# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/service/payments/payments_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api.entity import billing_info_pb2 as api_dot_entity_dot_billing__info__pb2
from layerapi.api.entity import payment_info_pb2 as api_dot_entity_dot_payment__info__pb2
from layerapi.api import ids_pb2 as api_dot_ids__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'api/service/payments/payments_api.proto\x12\x03\x61pi\x1a\x1d\x61pi/entity/billing_info.proto\x1a\x1d\x61pi/entity/payment_info.proto\x1a\rapi/ids.proto\"^\n\x1b\x43reateStripeCustomerRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\"\n\naccount_id\x18\x03 \x01(\x0b\x32\x0e.api.AccountId\"/\n\x1c\x43reateStripeCustomerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"F\n CreateStripeSetupIntentIdRequest\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\"]\n!CreateStripeSetupIntentIdResponse\x12\x38\n\x16stripe_setup_intent_id\x18\x01 \x01(\x0b\x32\x18.api.StripeSetupIntentId\"\x84\x01\n SaveStripePaymentMethodIdRequest\x12<\n\x18stripe_payment_method_id\x18\x01 \x01(\x0b\x32\x1a.api.StripePaymentMethodId\x12\"\n\naccount_id\x18\x02 \x01(\x0b\x32\x0e.api.AccountId\"K\n!SaveStripePaymentMethodIdResponse\x12&\n\x0c\x62illing_info\x18\x01 \x01(\x0b\x32\x10.api.BillingInfo\"[\n\x1bGetStripeBillingInfoRequest\x12<\n\x18stripe_payment_method_id\x18\x01 \x01(\x0b\x32\x1a.api.StripePaymentMethodId\"F\n\x1cGetStripeBillingInfoResponse\x12&\n\x0c\x62illing_info\x18\x01 \x01(\x0b\x32\x10.api.BillingInfo\"E\n\x1fGetStripePaymentMethodIdRequest\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\"`\n GetStripePaymentMethodIdResponse\x12<\n\x18stripe_payment_method_id\x18\x01 \x01(\x0b\x32\x1a.api.StripePaymentMethodId\"F\n DeleteStripePaymentMethodRequest\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\"4\n!DeleteStripePaymentMethodResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"B\n\x1cGetStripePaymentsListRequest\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\"C\n\x1dGetStripePaymentsListResponse\x12\"\n\x08payments\x18\x01 \x03(\x0b\x32\x10.api.PaymentInfo\"l\n\x1eUpdateStripeBillingInfoRequest\x12&\n\x0c\x62illing_info\x18\x01 \x01(\x0b\x32\x10.api.BillingInfo\x12\"\n\naccount_id\x18\x02 \x01(\x0b\x32\x0e.api.AccountId\"2\n\x1fUpdateStripeBillingInfoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"?\n\x19GetLastPaymentInfoRequest\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\"V\n\x1aGetLastPaymentInfoResponse\x12!\n\x07payment\x18\x01 \x01(\x0b\x32\x10.api.PaymentInfo\x12\x15\n\rerror_message\x18\x02 \x01(\t\"O\n\x15\x43hargeCustomerRequest\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\x12\x12\n\nproduct_id\x18\x02 \x01(\t\"&\n\x16\x43hargeCustomerResponse\x12\x0c\n\x04paid\x18\x01 \x01(\x08\x32\xdc\x07\n\x0bPaymentsAPI\x12[\n\x14\x43reateStripeCustomer\x12 .api.CreateStripeCustomerRequest\x1a!.api.CreateStripeCustomerResponse\x12j\n\x19\x43reateStripeSetupIntentId\x12%.api.CreateStripeSetupIntentIdRequest\x1a&.api.CreateStripeSetupIntentIdResponse\x12j\n\x19SaveStripePaymentMethodId\x12%.api.SaveStripePaymentMethodIdRequest\x1a&.api.SaveStripePaymentMethodIdResponse\x12[\n\x14GetStripeBillingInfo\x12 .api.GetStripeBillingInfoRequest\x1a!.api.GetStripeBillingInfoResponse\x12g\n\x18GetStripePaymentMethodId\x12$.api.GetStripePaymentMethodIdRequest\x1a%.api.GetStripePaymentMethodIdResponse\x12j\n\x19\x44\x65leteStripePaymentMethod\x12%.api.DeleteStripePaymentMethodRequest\x1a&.api.DeleteStripePaymentMethodResponse\x12^\n\x15GetStripePaymentsList\x12!.api.GetStripePaymentsListRequest\x1a\".api.GetStripePaymentsListResponse\x12\x64\n\x17UpdateStripeBillingInfo\x12#.api.UpdateStripeBillingInfoRequest\x1a$.api.UpdateStripeBillingInfoResponse\x12U\n\x12GetLastPaymentInfo\x12\x1e.api.GetLastPaymentInfoRequest\x1a\x1f.api.GetLastPaymentInfoResponse\x12I\n\x0e\x43hargeCustomer\x12\x1a.api.ChargeCustomerRequest\x1a\x1b.api.ChargeCustomerResponseB#\n\rcom.layer.apiB\x10PaymentsApiProtoP\x01\x62\x06proto3')



_CREATESTRIPECUSTOMERREQUEST = DESCRIPTOR.message_types_by_name['CreateStripeCustomerRequest']
_CREATESTRIPECUSTOMERRESPONSE = DESCRIPTOR.message_types_by_name['CreateStripeCustomerResponse']
_CREATESTRIPESETUPINTENTIDREQUEST = DESCRIPTOR.message_types_by_name['CreateStripeSetupIntentIdRequest']
_CREATESTRIPESETUPINTENTIDRESPONSE = DESCRIPTOR.message_types_by_name['CreateStripeSetupIntentIdResponse']
_SAVESTRIPEPAYMENTMETHODIDREQUEST = DESCRIPTOR.message_types_by_name['SaveStripePaymentMethodIdRequest']
_SAVESTRIPEPAYMENTMETHODIDRESPONSE = DESCRIPTOR.message_types_by_name['SaveStripePaymentMethodIdResponse']
_GETSTRIPEBILLINGINFOREQUEST = DESCRIPTOR.message_types_by_name['GetStripeBillingInfoRequest']
_GETSTRIPEBILLINGINFORESPONSE = DESCRIPTOR.message_types_by_name['GetStripeBillingInfoResponse']
_GETSTRIPEPAYMENTMETHODIDREQUEST = DESCRIPTOR.message_types_by_name['GetStripePaymentMethodIdRequest']
_GETSTRIPEPAYMENTMETHODIDRESPONSE = DESCRIPTOR.message_types_by_name['GetStripePaymentMethodIdResponse']
_DELETESTRIPEPAYMENTMETHODREQUEST = DESCRIPTOR.message_types_by_name['DeleteStripePaymentMethodRequest']
_DELETESTRIPEPAYMENTMETHODRESPONSE = DESCRIPTOR.message_types_by_name['DeleteStripePaymentMethodResponse']
_GETSTRIPEPAYMENTSLISTREQUEST = DESCRIPTOR.message_types_by_name['GetStripePaymentsListRequest']
_GETSTRIPEPAYMENTSLISTRESPONSE = DESCRIPTOR.message_types_by_name['GetStripePaymentsListResponse']
_UPDATESTRIPEBILLINGINFOREQUEST = DESCRIPTOR.message_types_by_name['UpdateStripeBillingInfoRequest']
_UPDATESTRIPEBILLINGINFORESPONSE = DESCRIPTOR.message_types_by_name['UpdateStripeBillingInfoResponse']
_GETLASTPAYMENTINFOREQUEST = DESCRIPTOR.message_types_by_name['GetLastPaymentInfoRequest']
_GETLASTPAYMENTINFORESPONSE = DESCRIPTOR.message_types_by_name['GetLastPaymentInfoResponse']
_CHARGECUSTOMERREQUEST = DESCRIPTOR.message_types_by_name['ChargeCustomerRequest']
_CHARGECUSTOMERRESPONSE = DESCRIPTOR.message_types_by_name['ChargeCustomerResponse']
CreateStripeCustomerRequest = _reflection.GeneratedProtocolMessageType('CreateStripeCustomerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTRIPECUSTOMERREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateStripeCustomerRequest)
  })
_sym_db.RegisterMessage(CreateStripeCustomerRequest)

CreateStripeCustomerResponse = _reflection.GeneratedProtocolMessageType('CreateStripeCustomerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTRIPECUSTOMERRESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateStripeCustomerResponse)
  })
_sym_db.RegisterMessage(CreateStripeCustomerResponse)

CreateStripeSetupIntentIdRequest = _reflection.GeneratedProtocolMessageType('CreateStripeSetupIntentIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTRIPESETUPINTENTIDREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateStripeSetupIntentIdRequest)
  })
_sym_db.RegisterMessage(CreateStripeSetupIntentIdRequest)

CreateStripeSetupIntentIdResponse = _reflection.GeneratedProtocolMessageType('CreateStripeSetupIntentIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTRIPESETUPINTENTIDRESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateStripeSetupIntentIdResponse)
  })
_sym_db.RegisterMessage(CreateStripeSetupIntentIdResponse)

SaveStripePaymentMethodIdRequest = _reflection.GeneratedProtocolMessageType('SaveStripePaymentMethodIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVESTRIPEPAYMENTMETHODIDREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.SaveStripePaymentMethodIdRequest)
  })
_sym_db.RegisterMessage(SaveStripePaymentMethodIdRequest)

SaveStripePaymentMethodIdResponse = _reflection.GeneratedProtocolMessageType('SaveStripePaymentMethodIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVESTRIPEPAYMENTMETHODIDRESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.SaveStripePaymentMethodIdResponse)
  })
_sym_db.RegisterMessage(SaveStripePaymentMethodIdResponse)

GetStripeBillingInfoRequest = _reflection.GeneratedProtocolMessageType('GetStripeBillingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRIPEBILLINGINFOREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetStripeBillingInfoRequest)
  })
_sym_db.RegisterMessage(GetStripeBillingInfoRequest)

GetStripeBillingInfoResponse = _reflection.GeneratedProtocolMessageType('GetStripeBillingInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRIPEBILLINGINFORESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetStripeBillingInfoResponse)
  })
_sym_db.RegisterMessage(GetStripeBillingInfoResponse)

GetStripePaymentMethodIdRequest = _reflection.GeneratedProtocolMessageType('GetStripePaymentMethodIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRIPEPAYMENTMETHODIDREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetStripePaymentMethodIdRequest)
  })
_sym_db.RegisterMessage(GetStripePaymentMethodIdRequest)

GetStripePaymentMethodIdResponse = _reflection.GeneratedProtocolMessageType('GetStripePaymentMethodIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRIPEPAYMENTMETHODIDRESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetStripePaymentMethodIdResponse)
  })
_sym_db.RegisterMessage(GetStripePaymentMethodIdResponse)

DeleteStripePaymentMethodRequest = _reflection.GeneratedProtocolMessageType('DeleteStripePaymentMethodRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESTRIPEPAYMENTMETHODREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.DeleteStripePaymentMethodRequest)
  })
_sym_db.RegisterMessage(DeleteStripePaymentMethodRequest)

DeleteStripePaymentMethodResponse = _reflection.GeneratedProtocolMessageType('DeleteStripePaymentMethodResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESTRIPEPAYMENTMETHODRESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.DeleteStripePaymentMethodResponse)
  })
_sym_db.RegisterMessage(DeleteStripePaymentMethodResponse)

GetStripePaymentsListRequest = _reflection.GeneratedProtocolMessageType('GetStripePaymentsListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRIPEPAYMENTSLISTREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetStripePaymentsListRequest)
  })
_sym_db.RegisterMessage(GetStripePaymentsListRequest)

GetStripePaymentsListResponse = _reflection.GeneratedProtocolMessageType('GetStripePaymentsListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTRIPEPAYMENTSLISTRESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetStripePaymentsListResponse)
  })
_sym_db.RegisterMessage(GetStripePaymentsListResponse)

UpdateStripeBillingInfoRequest = _reflection.GeneratedProtocolMessageType('UpdateStripeBillingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTRIPEBILLINGINFOREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateStripeBillingInfoRequest)
  })
_sym_db.RegisterMessage(UpdateStripeBillingInfoRequest)

UpdateStripeBillingInfoResponse = _reflection.GeneratedProtocolMessageType('UpdateStripeBillingInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTRIPEBILLINGINFORESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateStripeBillingInfoResponse)
  })
_sym_db.RegisterMessage(UpdateStripeBillingInfoResponse)

GetLastPaymentInfoRequest = _reflection.GeneratedProtocolMessageType('GetLastPaymentInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTPAYMENTINFOREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetLastPaymentInfoRequest)
  })
_sym_db.RegisterMessage(GetLastPaymentInfoRequest)

GetLastPaymentInfoResponse = _reflection.GeneratedProtocolMessageType('GetLastPaymentInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTPAYMENTINFORESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetLastPaymentInfoResponse)
  })
_sym_db.RegisterMessage(GetLastPaymentInfoResponse)

ChargeCustomerRequest = _reflection.GeneratedProtocolMessageType('ChargeCustomerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHARGECUSTOMERREQUEST,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ChargeCustomerRequest)
  })
_sym_db.RegisterMessage(ChargeCustomerRequest)

ChargeCustomerResponse = _reflection.GeneratedProtocolMessageType('ChargeCustomerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHARGECUSTOMERRESPONSE,
  '__module__' : 'api.service.payments.payments_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ChargeCustomerResponse)
  })
_sym_db.RegisterMessage(ChargeCustomerResponse)

_PAYMENTSAPI = DESCRIPTOR.services_by_name['PaymentsAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiB\020PaymentsApiProtoP\001'
  _CREATESTRIPECUSTOMERREQUEST._serialized_start=125
  _CREATESTRIPECUSTOMERREQUEST._serialized_end=219
  _CREATESTRIPECUSTOMERRESPONSE._serialized_start=221
  _CREATESTRIPECUSTOMERRESPONSE._serialized_end=268
  _CREATESTRIPESETUPINTENTIDREQUEST._serialized_start=270
  _CREATESTRIPESETUPINTENTIDREQUEST._serialized_end=340
  _CREATESTRIPESETUPINTENTIDRESPONSE._serialized_start=342
  _CREATESTRIPESETUPINTENTIDRESPONSE._serialized_end=435
  _SAVESTRIPEPAYMENTMETHODIDREQUEST._serialized_start=438
  _SAVESTRIPEPAYMENTMETHODIDREQUEST._serialized_end=570
  _SAVESTRIPEPAYMENTMETHODIDRESPONSE._serialized_start=572
  _SAVESTRIPEPAYMENTMETHODIDRESPONSE._serialized_end=647
  _GETSTRIPEBILLINGINFOREQUEST._serialized_start=649
  _GETSTRIPEBILLINGINFOREQUEST._serialized_end=740
  _GETSTRIPEBILLINGINFORESPONSE._serialized_start=742
  _GETSTRIPEBILLINGINFORESPONSE._serialized_end=812
  _GETSTRIPEPAYMENTMETHODIDREQUEST._serialized_start=814
  _GETSTRIPEPAYMENTMETHODIDREQUEST._serialized_end=883
  _GETSTRIPEPAYMENTMETHODIDRESPONSE._serialized_start=885
  _GETSTRIPEPAYMENTMETHODIDRESPONSE._serialized_end=981
  _DELETESTRIPEPAYMENTMETHODREQUEST._serialized_start=983
  _DELETESTRIPEPAYMENTMETHODREQUEST._serialized_end=1053
  _DELETESTRIPEPAYMENTMETHODRESPONSE._serialized_start=1055
  _DELETESTRIPEPAYMENTMETHODRESPONSE._serialized_end=1107
  _GETSTRIPEPAYMENTSLISTREQUEST._serialized_start=1109
  _GETSTRIPEPAYMENTSLISTREQUEST._serialized_end=1175
  _GETSTRIPEPAYMENTSLISTRESPONSE._serialized_start=1177
  _GETSTRIPEPAYMENTSLISTRESPONSE._serialized_end=1244
  _UPDATESTRIPEBILLINGINFOREQUEST._serialized_start=1246
  _UPDATESTRIPEBILLINGINFOREQUEST._serialized_end=1354
  _UPDATESTRIPEBILLINGINFORESPONSE._serialized_start=1356
  _UPDATESTRIPEBILLINGINFORESPONSE._serialized_end=1406
  _GETLASTPAYMENTINFOREQUEST._serialized_start=1408
  _GETLASTPAYMENTINFOREQUEST._serialized_end=1471
  _GETLASTPAYMENTINFORESPONSE._serialized_start=1473
  _GETLASTPAYMENTINFORESPONSE._serialized_end=1559
  _CHARGECUSTOMERREQUEST._serialized_start=1561
  _CHARGECUSTOMERREQUEST._serialized_end=1640
  _CHARGECUSTOMERRESPONSE._serialized_start=1642
  _CHARGECUSTOMERRESPONSE._serialized_end=1680
  _PAYMENTSAPI._serialized_start=1683
  _PAYMENTSAPI._serialized_end=2671
# @@protoc_insertion_point(module_scope)
