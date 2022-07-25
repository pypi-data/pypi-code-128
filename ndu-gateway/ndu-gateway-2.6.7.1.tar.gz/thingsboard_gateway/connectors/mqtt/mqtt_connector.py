#     Copyright 2022. ThingsBoard
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

import random
import ssl
import string
from queue import Queue
from re import fullmatch, match, search
from threading import Thread
from time import sleep, time

import simplejson
from paho.mqtt.client import Client

from thingsboard_gateway.connectors.connector import Connector, log
from thingsboard_gateway.tb_utility.tb_loader import TBModuleLoader
from thingsboard_gateway.tb_utility.tb_utility import TBUtility


class MqttConnector(Connector, Thread):
    def __init__(self, gateway, config, connector_type, hostIP, clientID, user, password):
        super().__init__()

        self.__gateway = gateway  # Reference to TB Gateway
        self._connector_type = connector_type  # Should be "mqtt"
        self.config = config  # mqtt.json contents

        self.__log = log
        self.statistics = {'MessagesReceived': 0, 'MessagesSent': 0}
        self.__subscribes_sent = {}

        # Extract main sections from configuration ---------------------------------------------------------------------
        self.__broker = config.get('broker')
        self.__hostIP = hostIP
        log.info("MQTT CONNECTOR: %s ", hostIP)
        
        self.__mapping = []
        self.__server_side_rpc = []
        self.__connect_requests = []
        self.__disconnect_requests = []
        self.__attribute_requests = []
        self.__attribute_updates = []
        self.lastDataDict = {}
        self.lastDataDict[clientID] = {}
        self.initLastDataDict(clientID)
        mandatory_keys = {
            "mapping": ['topicFilter', 'converter'],
            # "serverSideRpc": ['deviceNameFilter', 'methodFilter', 'requestTopicExpression', 'valueExpression'],
            # "connectRequests": ['topicFilter'],
            # "disconnectRequests": ['topicFilter'],
            # "attributeRequests": ['topicFilter', 'topicExpression', 'valueExpression'],
            # "attributeUpdates": ['deviceNameFilter', 'attributeFilter', 'topicExpression', 'valueExpression']
        }

        # Mappings, i.e., telemetry/attributes-push handlers provided by user via configuration file
        self.load_handlers('mapping', mandatory_keys['mapping'], self.__mapping)

        # RPCs, i.e., remote procedure calls (ThingsBoard towards devices) handlers
        #self.load_handlers('serverSideRpc', mandatory_keys['serverSideRpc'], self.__server_side_rpc)

        # Connect requests, i.e., telling ThingsBoard that a device is online even if it does not post telemetry
        #self.load_handlers('connectRequests', mandatory_keys['connectRequests'], self.__connect_requests)

        # Disconnect requests, i.e., telling ThingsBoard that a device is offline even if keep-alive has not expired yet
        #self.load_handlers('disconnectRequests', mandatory_keys['disconnectRequests'], self.__disconnect_requests)

        # Shared attributes direct requests, i.e., asking ThingsBoard for some shared attribute value
        #self.load_handlers('attributeRequests', mandatory_keys['attributeRequests'], self.__attribute_requests)

        # Attributes updates requests, i.e., asking ThingsBoard to send updates about an attribute
        #self.load_handlers('attributeUpdates', mandatory_keys['attributeUpdates'], self.__attribute_updates)

        # Setup topic substitution lists for each class of handlers ----------------------------------------------------
        self.__mapping_sub_topics = {}
        self.__connect_requests_sub_topics = {}
        self.__disconnect_requests_sub_topics = {}
        self.__attribute_requests_sub_topics = {}

        # Set up external MQTT broker connection -----------------------------------------------------------------------
        self.__client_ID = clientID #self.__broker.get("clientId", ''.join(random.choice(string.ascii_lowercase) for _ in range(23)))
        self._client = Client(self.__client_ID)
        self.setName(self.__client_ID + " " + hostIP)
        #config.get("name", self.__broker.get("name", 'Mqtt Broker ' + ''.join(random.choice(string.ascii_lowercase) for _ in range(5)))))

        self._client.username_pw_set(user, password)

        # Set up external MQTT broker callbacks ------------------------------------------------------------------------
        self._client.on_connect = self._on_connect
        self._client.on_message = self._on_message
        self._client.on_subscribe = self._on_subscribe
        self._client.on_disconnect = self._on_disconnect
        # self._client.on_log = self._on_log

        # Set up lifecycle flags ---------------------------------------------------------------------------------------
        self._connected = False
        self.__stopped = False
        self.daemon = True

        self.__msg_queue = Queue()
        self.__workers_thread_pool = []
        self.__max_msg_number_for_worker = config.get(
            'maxMessageNumberPerWorker', 10)
        self.__max_number_of_workers = config.get('maxNumberOfWorkers', 100)

    def load_handlers(self, handler_flavor, mandatory_keys, accepted_handlers_list):
        if handler_flavor not in self.config:
            self.__log.error(
                "'%s' section missing from configuration", handler_flavor)
        else:
            for handler in self.config.get(handler_flavor):
                discard = False

                for key in mandatory_keys:
                    if key not in handler:
                        # Will report all missing fields to user before discarding the entry => no break here
                        discard = True
                        self.__log.error("Mandatory key '%s' missing from %s handler: %s",
                                         key, handler_flavor, simplejson.dumps(handler))
                    else:
                        self.__log.debug("Mandatory key '%s' found in %s handler: %s",
                                         key, handler_flavor, simplejson.dumps(handler))

                if discard:
                    self.__log.error("%s handler is missing some mandatory keys => rejected: %s",
                                     handler_flavor, simplejson.dumps(handler))
                else:
                    accepted_handlers_list.append(handler)
                    self.__log.debug("%s handler has all mandatory keys => accepted: %s",
                                     handler_flavor, simplejson.dumps(handler))

            self.__log.info("Number of accepted %s handlers: %d",
                            handler_flavor,
                            len(accepted_handlers_list))

            self.__log.info("Number of rejected %s handlers: %d",
                            handler_flavor,
                            len(self.config.get(handler_flavor)) - len(accepted_handlers_list))

    def is_connected(self):
        return self._connected

    def open(self):
        self.__stopped = False
        self.start()

    def run(self):
        try:
            self.__connect()
        except Exception as e:
            self.__log.exception(e)
            try:
                self.close()
            except Exception as e:
                self.__log.exception(e)

        while True:
            if self.__stopped:
                break
            elif not self._connected:
                self.__connect()
            self.__threads_manager()
            sleep(.2)

    def __connect(self):
        while not self._connected and not self.__stopped:
            try:
                self._client.connect(self.__hostIP,
                                     self.__broker.get('port', 1883))
                self._client.loop_start()
                if not self._connected:
                    sleep(1)
            except ConnectionRefusedError as e:
                self.__log.error(e)
                sleep(10)

    def close(self):
        self.__stopped = True
        try:
            self._client.disconnect()
        except Exception as e:
            log.exception(e)
        self._client.loop_stop()
        self.__log.info('%s has been stopped.', self.get_name())

    def get_name(self):
        return self.name

    def __subscribe(self, topic, qos):
        message = self._client.subscribe(topic, qos)
        try:
            self.__subscribes_sent[message[1]] = topic
        except Exception as e:
            self.__log.exception(e)

    def _on_connect(self, client, userdata, flags, result_code, *extra_params):
        log.info("on connect")
        result_codes = {
            1: "incorrect protocol version",
            2: "invalid client identifier",
            3: "server unavailable",
            4: "bad username or password",
            5: "not authorised",
        }

        if result_code == 0:
            self._connected = True
            self.__log.info('%s connected to %s:%s - successfully.',
                            self.get_name(),
                            self.__hostIP,
                            self.__broker.get("port", "1883"))

            self.__log.debug("Client %s, userdata %s, flags %s, extra_params %s",
                             str(client),
                             str(userdata),
                             str(flags),
                             extra_params)

            self.__mapping_sub_topics = {}

            # Setup data upload requests handling ----------------------------------------------------------------------
            for mapping in self.__mapping:
                try:
                    # Load converter for this mapping entry ------------------------------------------------------------
                    # mappings are guaranteed to have topicFilter and converter fields. See __init__
                    default_converter_class_name = "JsonMqttUplinkConverter"
                    # Get converter class from "extension" parameter or default converter
                    converter_class_name = mapping["converter"].get(
                        "extension", default_converter_class_name)
                    # Find and load required class
                    module = TBModuleLoader.import_module(
                        self._connector_type, converter_class_name)
                    if module:
                        self.__log.debug('Converter %s for topic %s - found!', converter_class_name,
                                         mapping["topicFilter"])
                        converter = module(mapping)
                    else:
                        self.__log.error(
                            "Cannot find converter for %s topic", mapping["topicFilter"])
                        continue

                    # Setup regexp topic acceptance list ---------------------------------------------------------------
                    regex_topic = TBUtility.topic_to_regex(
                        mapping["topicFilter"])

                    # There may be more than one converter per topic, so I'm using vectors
                    if not self.__mapping_sub_topics.get(regex_topic):
                        self.__mapping_sub_topics[regex_topic] = []

                    self.__mapping_sub_topics[regex_topic].append(converter)

                    # Subscribe to appropriate topic -------------------------------------------------------------------
                    self.__subscribe(
                        mapping["topicFilter"], mapping.get("subscriptionQos", 1))

                    self.__log.info('Connector "%s" subscribe to %s',
                                    self.get_name(),
                                    TBUtility.regex_to_topic(regex_topic))

                except Exception as e:
                    self.__log.exception(e)

            # Setup connection requests handling -----------------------------------------------------------------------
            for request in [entry for entry in self.__connect_requests if entry is not None]:
                # requests are guaranteed to have topicFilter field. See __init__
                self.__subscribe(request["topicFilter"],
                                 request.get("subscriptionQos", 1))
                topic_filter = TBUtility.topic_to_regex(
                    request.get("topicFilter"))
                self.__connect_requests_sub_topics[topic_filter] = request

            # Setup disconnection requests handling --------------------------------------------------------------------
            for request in [entry for entry in self.__disconnect_requests if entry is not None]:
                # requests are guaranteed to have topicFilter field. See __init__
                self.__subscribe(request["topicFilter"],
                                 request.get("subscriptionQos", 1))
                topic_filter = TBUtility.topic_to_regex(
                    request.get("topicFilter"))
                self.__disconnect_requests_sub_topics[topic_filter] = request

            # Setup attributes requests handling -----------------------------------------------------------------------
            for request in [entry for entry in self.__attribute_requests if entry is not None]:
                # requests are guaranteed to have topicFilter field. See __init__
                self.__subscribe(request["topicFilter"],
                                 request.get("subscriptionQos", 1))
                topic_filter = TBUtility.topic_to_regex(
                    request.get("topicFilter"))
                self.__attribute_requests_sub_topics[topic_filter] = request
        else:
            if result_code in result_codes:
                self.__log.error("%s connection FAIL with error %s %s!", self.get_name(), result_code,
                                 result_codes[result_code])
            else:
                self.__log.error(
                    "%s connection FAIL with unknown error!", self.get_name())

    def _on_disconnect(self, *args):
        self._connected = False
        self.__log.debug('"%s" was disconnected. %s',
                         self.get_name(), str(args))

    def _on_log(self, *args):
        self.__log.debug(args)

    def _on_subscribe(self, _, __, mid, granted_qos, *args):
        log.info(args)
        try:
            if granted_qos[0] == 128:
                self.__log.error('"%s" subscription failed to topic %s subscription message id = %i',
                                 self.get_name(),
                                 self.__subscribes_sent.get(mid), mid)
            else:
                self.__log.info('"%s" subscription success to topic %s, subscription message id = %i',
                                self.get_name(),
                                self.__subscribes_sent.get(mid), mid)
        except Exception as e:
            self.__log.exception(e)

        # Success or not, remove this topic from the list of pending subscription requests
        if self.__subscribes_sent.get(mid) is not None:
            del self.__subscribes_sent[mid]

    def put_data_to_convert(self, converter, message, content) -> bool:
        if not self.__msg_queue.full():
            self.__msg_queue.put((converter.convert, message.topic, content, self.__client_ID), True, 100)
            return True
        return False

    def _save_converted_msg(self, topic, data):
        self.__gateway.send_to_storage(self.name, data)
        self.statistics['MessagesSent'] += 1
        self.__log.debug("Successfully converted message from topic %s", topic)

    def __threads_manager(self):
        if len(self.__workers_thread_pool) == 0:
            worker = MqttConnector.ConverterWorker(
                "Main", self.__msg_queue, self._save_converted_msg)
            self.__workers_thread_pool.append(worker)
            worker.start()

        number_of_needed_threads = round(
            self.__msg_queue.qsize() / self.__max_msg_number_for_worker, 0)
        threads_count = len(self.__workers_thread_pool)
        if number_of_needed_threads > threads_count < self.__max_number_of_workers:
            thread = MqttConnector.ConverterWorker(
                "Worker " + ''.join(random.choice(string.ascii_lowercase)
                                    for _ in range(5)), self.__msg_queue,
                self._save_converted_msg)
            self.__workers_thread_pool.append(thread)
            thread.start()
        elif number_of_needed_threads < threads_count and threads_count > 1:
            worker: MqttConnector.ConverterWorker = self.__workers_thread_pool[-1]
            if not worker.in_progress:
                worker.stopped = True
                self.__workers_thread_pool.remove(worker)

    def initLastDataDict(self, clientID):
        for element in self.config['mapping']:
            self.__log.info("FILTER: %s", element['topicFilter'])
            self.lastDataDict[clientID][element['topicFilter']] = {"ts": time(), "value": 1}
            self.__log.info(self.lastDataDict)
            #{'RTU003': {'/v2/rt.di.reg5': 1}}

    def checkTelemetryUpdate(self, clientID, topic, content):
        self.__log.info(self.lastDataDict)
        if self.lastDataDict[clientID][topic]['value'] == content:
                #return False if more than 1 minute has passed since last update
                if time() - self.lastDataDict[clientID][topic]['ts'] > self.config.get("update_interval_seconds", 60):
                    self.__log.info("Update: %s", content)
                    self.lastDataDict[clientID][topic]['ts'] = time()
                    self.lastDataDict[clientID][topic]['value'] = content
                    return False
                else:
                    self.__log.info("Same")
                    return True
        else:
            self.lastDataDict[clientID][topic]['value'] = content
            self.__log.info(self.lastDataDict)
            return False

    def _on_message(self, client, userdata, message):
        self.statistics['MessagesReceived'] += 1
        content = TBUtility.decode(message)
        if self.is_connected():
            if self.checkTelemetryUpdate(self.__client_ID, message.topic, content) is True:
                return
        # Check if message topic exists in mappings "i.e., I'm posting telemetry/attributes" ---------------------------
        topic_handlers = [
            regex for regex in self.__mapping_sub_topics if fullmatch(regex, message.topic)]

        if topic_handlers:
            # Note: every topic may be associated to one or more converter. This means that a single MQTT message
            # may produce more than one message towards ThingsBoard. This also means that I cannot return after
            # the first successful conversion: I got to use all the available ones.
            # I will use a flag to understand whether at least one converter succeeded
            request_handled = False

            for topic in topic_handlers:
                available_converters = self.__mapping_sub_topics[topic]
                for converter in available_converters:
                    try:
                        if isinstance(content, list):
                            for item in content:
                                request_handled = self.put_data_to_convert(
                                    converter, message, item)
                                self.__log.info(item)
                                self.__log.info(message)
                                if not request_handled:
                                    self.__log.error(
                                        'Cannot find converter for the topic:"%s"! Client: %s, User data: %s',
                                        message.topic,
                                        str(client),
                                        str(userdata))
                        else:
                            request_handled = self.put_data_to_convert(converter, message, content)
                            self.__log.info("%s", message)

                    except Exception as e:
                        log.exception(e)

            if not request_handled:
                self.__log.error('Cannot find converter for the topic:"%s"! Client: %s, User data: %s',
                                 message.topic,
                                 str(client),
                                 str(userdata))

            # Note: if I'm in this branch, this was for sure a telemetry/attribute push message
            # => Execution must end here both in case of failure and success
            return None

        # Check if message topic exists in connection handlers "i.e., I'm connecting a device" -------------------------
        topic_handlers = [regex for regex in self.__connect_requests_sub_topics if fullmatch(
            regex, message.topic)]

        if topic_handlers:
            for topic in topic_handlers:
                handler = self.__connect_requests_sub_topics[topic]

                found_device_name = None
                found_device_type = 'default'

                # Get device name, either from topic or from content
                if handler.get("deviceNameTopicExpression"):
                    device_name_match = search(
                        handler["deviceNameTopicExpression"], message.topic)
                    if device_name_match is not None:
                        found_device_name = device_name_match.group(0)
                elif handler.get("deviceNameJsonExpression"):
                    found_device_name = TBUtility.get_value(
                        handler["deviceNameJsonExpression"], content)

                # Get device type (if any), either from topic or from content
                if handler.get("deviceTypeTopicExpression"):
                    device_type_match = search(
                        handler["deviceTypeTopicExpression"], message.topic)
                    found_device_type = device_type_match.group(0) if device_type_match is not None else handler[
                        "deviceTypeTopicExpression"]
                elif handler.get("deviceTypeJsonExpression"):
                    found_device_type = TBUtility.get_value(
                        handler["deviceTypeJsonExpression"], content)

                if found_device_name is None:
                    self.__log.error(
                        "Device name missing from connection request")
                    continue

                # Note: device must be added even if it is already known locally: else ThingsBoard
                # will not send RPCs and attribute updates
                self.__log.info("Connecting device %s of type %s",
                                found_device_name, found_device_type)
                self.__gateway.add_device(
                    found_device_name, {"connector": self}, device_type=found_device_type)

            # Note: if I'm in this branch, this was for sure a connection message
            # => Execution must end here both in case of failure and success
            return None

        # Check if message topic exists in disconnection handlers "i.e., I'm disconnecting a device" -------------------
        topic_handlers = [regex for regex in self.__disconnect_requests_sub_topics if fullmatch(
            regex, message.topic)]
        if topic_handlers:
            for topic in topic_handlers:
                handler = self.__disconnect_requests_sub_topics[topic]

                found_device_name = None
                found_device_type = 'default'

                # Get device name, either from topic or from content
                if handler.get("deviceNameTopicExpression"):
                    device_name_match = search(
                        handler["deviceNameTopicExpression"], message.topic)
                    if device_name_match is not None:
                        found_device_name = device_name_match.group(0)
                elif handler.get("deviceNameJsonExpression"):
                    found_device_name = TBUtility.get_value(
                        handler["deviceNameJsonExpression"], content)

                # Get device type (if any), either from topic or from content
                if handler.get("deviceTypeTopicExpression"):
                    device_type_match = search(
                        handler["deviceTypeTopicExpression"], message.topic)
                    if device_type_match is not None:
                        found_device_type = device_type_match.group(0)
                elif handler.get("deviceTypeJsonExpression"):
                    found_device_type = TBUtility.get_value(
                        handler["deviceTypeJsonExpression"], content)

                if found_device_name is None:
                    self.__log.error(
                        "Device name missing from disconnection request")
                    continue

                if found_device_name in self.__gateway.get_devices():
                    self.__log.info("Disconnecting device %s of type %s",
                                    found_device_name, found_device_type)
                    self.__gateway.del_device(found_device_name)
                else:
                    self.__log.info(
                        "Device %s was not connected", found_device_name)

                break

            # Note: if I'm in this branch, this was for sure a disconnection message
            # => Execution must end here both in case of failure and success
            return None

        # Check if message topic exists in attribute request handlers "i.e., I'm asking for a shared attribute" --------
        topic_handlers = [regex for regex in self.__attribute_requests_sub_topics if fullmatch(
            regex, message.topic)]
        if topic_handlers:
            try:
                for topic in topic_handlers:
                    handler = self.__attribute_requests_sub_topics[topic]

                    found_device_name = None
                    found_attribute_name = None

                    # Get device name, either from topic or from content
                    if handler.get("deviceNameTopicExpression"):
                        device_name_match = search(
                            handler["deviceNameTopicExpression"], message.topic)
                        if device_name_match is not None:
                            found_device_name = device_name_match.group(0)
                    elif handler.get("deviceNameJsonExpression"):
                        found_device_name = TBUtility.get_value(
                            handler["deviceNameJsonExpression"], content)

                    # Get attribute name, either from topic or from content
                    if handler.get("attributeNameTopicExpression"):
                        attribute_name_match = search(
                            handler["attributeNameTopicExpression"], message.topic)
                        if attribute_name_match is not None:
                            found_attribute_name = attribute_name_match.group(
                                0)
                    elif handler.get("attributeNameJsonExpression"):
                        found_attribute_name = TBUtility.get_value(
                            handler["attributeNameJsonExpression"], content)

                    if found_device_name is None:
                        self.__log.error(
                            "Device name missing from attribute request")
                        continue

                    if found_attribute_name is None:
                        self.__log.error(
                            "Attribute name missing from attribute request")
                        continue

                    self.__log.info("Will retrieve attribute %s of %s",
                                    found_attribute_name, found_device_name)
                    self.__gateway.tb_client.client.gw_request_shared_attributes(
                        found_device_name,
                        [found_attribute_name],
                        lambda data, *args: self.notify_attribute(
                            data,
                            found_attribute_name,
                            handler.get("topicExpression"),
                            handler.get("valueExpression"),
                            handler.get('retain', False)))

                    break

            except Exception as e:
                log.exception(e)

            # Note: if I'm in this branch, this was for sure an attribute request message
            # => Execution must end here both in case of failure and success
            return None

        # Check if message topic exists in RPC handlers ----------------------------------------------------------------
        # The gateway is expecting for this message => no wildcards here, the topic must be evaluated as is

        if self.__gateway.is_rpc_in_progress(message.topic):
            log.info("RPC response arrived. Forwarding it to thingsboard.")
            self.__gateway.rpc_with_reply_processing(message.topic, content)
            return None

        self.__log.debug("Received message to topic \"%s\" with unknown interpreter data: \n\n\"%s\"",
                         message.topic,
                         content)

    def notify_attribute(self, incoming_data, attribute_name, topic_expression, value_expression, retain):
        if incoming_data.get("device") is None or incoming_data.get("value") is None:
            return

        device_name = incoming_data.get("device")
        attribute_value = incoming_data.get("value")

        topic = topic_expression \
            .replace("${deviceName}", str(device_name)) \
            .replace("${attributeKey}", str(attribute_name))

        data = value_expression.replace("${attributeKey}", str(attribute_name)) \
            .replace("${attributeValue}", str(attribute_value))

        self._client.publish(topic, data, retain=retain).wait_for_publish()

    def on_attributes_update(self, content):
        if self.__attribute_updates:
            for attribute_update in self.__attribute_updates:
                if match(attribute_update["deviceNameFilter"], content["device"]):
                    for attribute_key in content["data"]:
                        if match(attribute_update["attributeFilter"], attribute_key):
                            try:
                                topic = attribute_update["topicExpression"] \
                                    .replace("${deviceName}", str(content["device"])) \
                                    .replace("${attributeKey}", str(attribute_key)) \
                                    .replace("${attributeValue}", str(content["data"][attribute_key]))
                            except KeyError as e:
                                log.exception(
                                    "Cannot form topic, key %s - not found", e)
                                raise e
                            try:
                                data = attribute_update["valueExpression"] \
                                    .replace("${attributeKey}", str(attribute_key)) \
                                    .replace("${attributeValue}", str(content["data"][attribute_key]))
                            except KeyError as e:
                                log.exception(
                                    "Cannot form topic, key %s - not found", e)
                                raise e
                            self._client.publish(topic, data,
                                                 retain=attribute_update.get('retain', False)).wait_for_publish()
                            self.__log.debug("Attribute Update data: %s for device %s to topic: %s", data,
                                             content["device"], topic)
                        else:
                            self.__log.error(
                                "Cannot find attributeName by filter in message with data: %s", content)
                else:
                    self.__log.error(
                        "Cannot find deviceName by filter in message with data: %s", content)
        else:
            self.__log.error("Attribute updates config not found.")

    def server_side_rpc_handler(self, content):
        self.__log.info("Incoming server-side RPC: %s", content)

        # Check whether one of my RPC handlers can handle this request
        for rpc_config in self.__server_side_rpc:
            if search(rpc_config["deviceNameFilter"], content["device"]) \
                    and search(rpc_config["methodFilter"], content["data"]["method"]) is not None:

                # This handler seems able to handle the request
                self.__log.info("Candidate RPC handler found")

                expects_response = rpc_config.get("responseTopicExpression")
                defines_timeout = rpc_config.get("responseTimeout")

                # 2-way RPC setup
                if expects_response and defines_timeout:
                    expected_response_topic = rpc_config["responseTopicExpression"] \
                        .replace("${deviceName}", str(content["device"])) \
                        .replace("${methodName}", str(content["data"]["method"])) \
                        .replace("${requestId}", str(content["data"]["id"]))

                    expected_response_topic = TBUtility.replace_params_tags(
                        expected_response_topic, content)

                    timeout = time() * 1000 + rpc_config.get("responseTimeout")

                    # Start listenting on the response topic
                    self.__log.info("Subscribing to: %s",
                                    expected_response_topic)
                    self.__subscribe(expected_response_topic,
                                     rpc_config.get("responseTopicQoS", 1))

                    # Wait for subscription to be carried out
                    sub_response_timeout = 10

                    while expected_response_topic in self.__subscribes_sent.values():
                        sub_response_timeout -= 1
                        sleep(0.1)
                        if sub_response_timeout == 0:
                            break

                    # Ask the gateway to enqueue this as an RPC response
                    self.__gateway.register_rpc_request_timeout(content,
                                                                timeout,
                                                                expected_response_topic,
                                                                self.rpc_cancel_processing)

                    # Wait for RPC to be successfully enqueued, which never fails.
                    while self.__gateway.is_rpc_in_progress(expected_response_topic):
                        sleep(0.1)

                elif expects_response and not defines_timeout:
                    self.__log.info(
                        "2-way RPC without timeout: treating as 1-way")

                # Actually reach out for the device
                request_topic: str = rpc_config.get("requestTopicExpression") \
                    .replace("${deviceName}", str(content["device"])) \
                    .replace("${methodName}", str(content["data"]["method"])) \
                    .replace("${requestId}", str(content["data"]["id"]))

                request_topic = TBUtility.replace_params_tags(
                    request_topic, content)

                data_to_send_tags = TBUtility.get_values(rpc_config.get('valueExpression'), content['data'],
                                                         'params',
                                                         get_tag=True)
                data_to_send_values = TBUtility.get_values(rpc_config.get('valueExpression'), content['data'],
                                                           'params',
                                                           expression_instead_none=True)

                data_to_send = rpc_config.get('valueExpression')
                for (tag, value) in zip(data_to_send_tags, data_to_send_values):
                    data_to_send = data_to_send.replace(
                        '${' + tag + '}', str(value))

                try:
                    self.__log.info("Publishing to: %s with data %s",
                                    request_topic, data_to_send)
                    self._client.publish(
                        request_topic, data_to_send, retain=rpc_config.get('retain', False))

                    if not expects_response or not defines_timeout:
                        self.__log.info(
                            "One-way RPC: sending ack to ThingsBoard immediately")
                        self.__gateway.send_rpc_reply(device=content["device"], req_id=content["data"]["id"],
                                                      success_sent=True)

                    # Everything went out smoothly: RPC is served
                    return

                except Exception as e:
                    self.__log.exception(e)

        self.__log.error("RPC not handled: %s", content)

    def rpc_cancel_processing(self, topic):
        log.info("RPC canceled or terminated. Unsubscribing from %s", topic)
        self._client.unsubscribe(topic)

    class ConverterWorker(Thread):
        def __init__(self, name, incoming_queue, send_result):
            super().__init__()
            self.stopped = False
            self.setName(name)
            self.setDaemon(True)
            self.__msg_queue = incoming_queue
            self.in_progress = False
            self.__send_result = send_result

        def run(self):
            while not self.stopped:
                if not self.__msg_queue.empty():
                    self.in_progress = True
                    convert_function, config, incoming_data, deviceID = self.__msg_queue.get(True, 100)
                    converted_data = convert_function(config, incoming_data, deviceID)
                    log.debug(converted_data)
                    self.__send_result(config, converted_data)
                    self.in_progress = False
                else:
                    sleep(.2)
