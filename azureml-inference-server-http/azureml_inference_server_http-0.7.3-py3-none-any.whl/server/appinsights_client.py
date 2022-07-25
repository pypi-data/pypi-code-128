import datetime
import json
import logging
import os
import sys
import time

import flask
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace import samplers
from opencensus.trace.span import SpanKind
from opencensus.trace.tracer import Tracer


# Amount of time we wait before exiting the application when errors occur for exception log sending
WAIT_EXCEPTION_UPLOAD_IN_SECONDS = 30


class AppInsightsClient(object):
    """Batching parameters, whichever of the below conditions gets hit first will trigger a send.
    send_interval: interval in seconds
    send_buffer_size: max number of items to batch before sending
    """

    send_interval = 5.0
    send_buffer_size = 100

    def __init__(self):
        self.enabled = False
        self._model_ids = self._get_model_ids()

        if os.getenv("AML_APP_INSIGHTS_ENABLED") == "true" and "AML_APP_INSIGHTS_KEY" in os.environ:
            try:
                instrumentation_key = os.getenv("AML_APP_INSIGHTS_KEY")
                self.logger = logging.getLogger(__name__)
                self.logger.setLevel("INFO")
                azureLogHandler = AzureLogHandler(
                    instrumentation_key=instrumentation_key,
                    export_interval=AppInsightsClient.send_interval,
                    max_batch_size=AppInsightsClient.send_buffer_size,
                )
                self.logger.addHandler(azureLogHandler)
                azureExporter = AzureExporter(
                    instrumentation_key=instrumentation_key,
                    export_interval=AppInsightsClient.send_interval,
                    max_batch_size=AppInsightsClient.send_buffer_size,
                )
                self.tracer = Tracer(
                    exporter=azureExporter,
                    sampler=samplers.AlwaysOnSampler(),
                )
                self._container_id = os.getenv("HOSTNAME", "Unknown")
                self.enabled = True
            except Exception as ex:
                self.log_app_insights_exception(ex)

        self.mdc_enabled = os.getenv("AML_MODEL_DC_STORAGE_ENABLED") == "true"
        self.log_response_enabled = os.getenv("APP_INSIGHTS_LOG_RESPONSE_ENABLED", "true").lower() == "true"

    def log_app_insights_exception(self, ex):
        print("Error logging to Application Insights:")
        print(ex)

    def send_model_data_log(self, request_id, client_request_id, model_input, prediction):
        try:
            if not self.enabled or not self.mdc_enabled:
                return
            properties = {
                "custom_dimensions": {
                    "Container Id": self._container_id,
                    "Request Id": request_id,
                    "Client Request Id": client_request_id,
                    "Workspace Name": os.environ.get("WORKSPACE_NAME", ""),
                    "Service Name": os.environ.get("SERVICE_NAME", ""),
                    "Models": self._model_ids,
                    "Input": json.dumps(model_input),
                    "Prediction": json.dumps(prediction),
                }
            }
            self.logger.info("model_data_collection", extra=properties)
        except Exception as ex:
            self.log_app_insights_exception(ex)

    def log_request(
        self,
        request: flask.Request,
        response: flask.Response,
        *,
        start_datetime: datetime.datetime,
        duration_ms: float,
        request_id: str,
        client_request_id: str,
    ) -> None:
        if not self.enabled:
            return

        if self.log_response_enabled:
            # Check if response payload can be converted to a valid string
            try:
                response_value = response.get_data(as_text=True)
            except (UnicodeDecodeError, AttributeError) as ex:
                self.log_app_insights_exception(ex)
                response_value = "Scoring request response payload is a non serializable object or raw binary"

            # We have to encode the response value (which is a string) as a JSON to maintain backwards compatibility.
            # This encodes '{"a": 12}' as '"{\\"a\\": 12}"'
            response_value = json.dumps(response_value)
        else:
            response_value = None

        successful = response.status_code < 400
        formatted_start_time = start_datetime.isoformat() + "Z"
        try:
            attributes = {
                "Container Id": self._container_id,
                "Request Id": request_id,
                "Client Request Id": client_request_id,
                "Response Value": response_value,
                "name": request.path,
                "url": request.url,
                "start_time": formatted_start_time,
                "duration": self._calc_duration(duration_ms),
                "resultCode": str(response.status_code),  # Cast to string to maintain backwards compatibility
                "success": successful,
                "http_method": request.method,
                "Workspace Name": os.environ.get("WORKSPACE_NAME", ""),
                "Service Name": os.environ.get("SERVICE_NAME", ""),
            }

            # Send the log to the requests table
            with self.tracer.span(name=request.path) as span:
                span.span_id = request_id
                span.start_time = formatted_start_time
                span.attributes = attributes
                span.span_kind = SpanKind.SERVER
        except Exception as ex:
            self.log_app_insights_exception(ex)

    def send_exception_log(self, exc_info, request_id="Unknown", client_request_id=""):
        try:
            if not self.enabled:
                return
            properties = {
                "custom_dimensions": {
                    "Container Id": self._container_id,
                    "Request Id": request_id,
                    "Client Request Id": client_request_id,
                }
            }

            self.logger.exception(exc_info, extra=properties)
        except Exception as ex:
            self.log_app_insights_exception(ex)

    def _calc_duration(self, duration):
        local_duration = duration or 0
        duration_parts = []
        for multiplier in [1000, 60, 60, 24]:
            duration_parts.append(local_duration % multiplier)
            local_duration //= multiplier
        duration_parts.reverse()
        formatted_duration = "%02d:%02d:%02d.%03d" % tuple(duration_parts)
        if local_duration:
            formatted_duration = "%d.%s" % (local_duration, formatted_duration)
        return formatted_duration

    def _get_model_ids(self):
        # Model information is stored in /var/azureml-app/model_config_map.json in AKS deployments. But, in ACI
        # deployments, that file does not exist due to a bug in container build-out code. Until the bug is fixed
        # /var/azureml-app/azureml-models will be used to enumerate all the models.
        # Details: https://msdata.visualstudio.com/Vienna/_workitems/edit/511413
        model_ids = []
        models_root_dir = os.path.join(os.environ.get("AML_APP_ROOT", "/var/azureml-app"), "azureml-models")
        try:
            models = [str(model) for model in os.listdir(models_root_dir)]

            for model in models:
                versions = [int(version) for version in os.listdir(os.path.join(models_root_dir, model))]
                ids = ["{}:{}".format(model, version) for version in versions]
                model_ids.extend(ids)
        except Exception:
            self.send_exception_log(sys.exc_info())

        return model_ids

    def wait_for_upload(self):
        if not self.enabled:
            return

        self.logger.info("Waiting for logs to be sent to Application Insights before exit.")
        self.logger.info(f"Waiting {WAIT_EXCEPTION_UPLOAD_IN_SECONDS} seconds for upload.")
        time.sleep(WAIT_EXCEPTION_UPLOAD_IN_SECONDS)
