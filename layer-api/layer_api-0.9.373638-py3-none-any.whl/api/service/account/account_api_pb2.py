# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/service/account/account_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api.entity import account_pb2 as api_dot_entity_dot_account__pb2
from layerapi.api.entity import account_view_pb2 as api_dot_entity_dot_account__view__pb2
from layerapi.api.entity import display_name_pb2 as api_dot_entity_dot_display__name__pb2
from layerapi.api.entity import image_pb2 as api_dot_entity_dot_image__pb2
from layerapi.api.entity import tier_pb2 as api_dot_entity_dot_tier__pb2
from layerapi.api.entity import tier_config_pb2 as api_dot_entity_dot_tier__config__pb2
from layerapi.api import ids_pb2 as api_dot_ids__pb2
from layerapi.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/service/account/account_api.proto\x12\x03\x61pi\x1a\x18\x61pi/entity/account.proto\x1a\x1d\x61pi/entity/account_view.proto\x1a\x1d\x61pi/entity/display_name.proto\x1a\x16\x61pi/entity/image.proto\x1a\x15\x61pi/entity/tier.proto\x1a\x1c\x61pi/entity/tier_config.proto\x1a\rapi/ids.proto\x1a\x17validate/validate.proto\"+\n\x1bGetAccountViewByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"F\n\x1cGetAccountViewByNameResponse\x12&\n\x0c\x61\x63\x63ount_view\x18\x01 \x01(\x0b\x32\x10.api.AccountView\"7\n\x19GetAccountViewByIdRequest\x12\x1a\n\x02id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\"D\n\x1aGetAccountViewByIdResponse\x12&\n\x0c\x61\x63\x63ount_view\x18\x01 \x01(\x0b\x32\x10.api.AccountView\"\x19\n\x17GetMyAccountViewRequest\"B\n\x18GetMyAccountViewResponse\x12&\n\x0c\x61\x63\x63ount_view\x18\x01 \x01(\x0b\x32\x10.api.AccountView\"u\n\x14\x43reateAccountRequest\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x03\x18\x32\x12 \n\x0c\x64isplay_name\x18\x02 \x01(\tB\n\xfa\x42\x07r\x05\x10\x03\x18\xff\x01\x12\"\n\rcreated_by_id\x18\x03 \x01(\x0b\x32\x0b.api.UserId\"?\n\x15\x43reateAccountResponse\x12&\n\x0c\x61\x63\x63ount_view\x18\x01 \x01(\x0b\x32\x10.api.AccountView\"\x81\x01\n CreateOrganizationAccountRequest\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x03\x18\x32\x12 \n\x0c\x64isplay_name\x18\x02 \x01(\tB\n\xfa\x42\x07r\x05\x10\x03\x18\xff\x01\x12\"\n\rcreated_by_id\x18\x03 \x01(\x0b\x32\x0b.api.UserId\"K\n!CreateOrganizationAccountResponse\x12&\n\x0c\x61\x63\x63ount_view\x18\x01 \x01(\x0b\x32\x10.api.AccountView\"S\n#ToggleDatasetLikeByMyAccountRequest\x12,\n\ndataset_id\x18\x01 \x01(\x0b\x32\x0e.api.DatasetIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"8\n$ToggleDatasetLikeByMyAccountResponse\x12\x10\n\x08is_liked\x18\x01 \x01(\x08\"Q\n!GetDatasetLikedByMyAccountRequest\x12,\n\ndataset_id\x18\x01 \x01(\x0b\x32\x0e.api.DatasetIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"6\n\"GetDatasetLikedByMyAccountResponse\x12\x10\n\x08is_liked\x18\x01 \x01(\x08\"M\n!ToggleModelLikeByMyAccountRequest\x12(\n\x08model_id\x18\x01 \x01(\x0b\x32\x0c.api.ModelIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"6\n\"ToggleModelLikeByMyAccountResponse\x12\x10\n\x08is_liked\x18\x01 \x01(\x08\"K\n\x1fGetModelLikedByMyAccountRequest\x12(\n\x08model_id\x18\x01 \x01(\x0b\x32\x0c.api.ModelIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"4\n GetModelLikedByMyAccountResponse\x12\x10\n\x08is_liked\x18\x01 \x01(\x08\"S\n#ToggleProjectLikeByMyAccountRequest\x12,\n\nproject_id\x18\x01 \x01(\x0b\x32\x0e.api.ProjectIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"8\n$ToggleProjectLikeByMyAccountResponse\x12\x10\n\x08is_liked\x18\x01 \x01(\x08\"Q\n!GetProjectLikedByMyAccountRequest\x12,\n\nproject_id\x18\x01 \x01(\x0b\x32\x0e.api.ProjectIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"6\n\"GetProjectLikedByMyAccountResponse\x12\x10\n\x08is_liked\x18\x01 \x01(\x08\"9\n\x13\x43reateApiKeyRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x14\n\x0credirect_uri\x18\x02 \x01(\t\"\'\n\x14\x43reateApiKeyResponse\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\"O\n\x1fGetTierConfigByAccountIdRequest\x12,\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"I\n GetTierConfigByAccountIdResponse\x12%\n\x0btier_config\x18\x01 \x01(\x0b\x32\x10.api.TierConfigs\"\x87\x01\n\x14UpdateAccountRequest\x12,\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x19\n\x05image\x18\x02 \x01(\x0b\x32\n.api.Image\x12&\n\x0c\x64isplay_name\x18\x03 \x01(\x0b\x32\x10.api.DisplayName\"E\n\x15UpdateAccountResponse\x12,\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"E\n\x15GetAccountByIdRequest\x12,\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"A\n\x16GetAccountByIdResponse\x12\'\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x0c.api.AccountB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"2\n\x17GetAccountByNameRequest\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x03\x18\x32\"C\n\x18GetAccountByNameResponse\x12\'\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x0c.api.AccountB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"r\n\x1a\x41ssignTierToAccountRequest\x12,\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12&\n\x07tier_id\x18\x02 \x01(\x0b\x32\x0b.api.TierIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"A\n\x1b\x41ssignTierToAccountResponse\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\"\x11\n\x0fGetTiersRequest\",\n\x10GetTiersResponse\x12\x18\n\x05tiers\x18\x01 \x03(\x0b\x32\t.api.Tier\"W\n$MigratePersonalLegacyAccountsRequest\x12\x0f\n\x07\x63onfirm\x18\x01 \x01(\x08\x12\x0f\n\x07\x64ry_run\x18\x02 \x01(\x08\x12\r\n\x05limit\x18\x03 \x01(\r\"\xf4\x03\n%MigratePersonalLegacyAccountsResponse\x12\x0f\n\x07\x64ry_run\x18\x01 \x01(\x08\x12\x19\n\x11\x61\x63\x63ounts_eligible\x18\x02 \x01(\r\x12\x17\n\x0frecords_updated\x18\x03 \x01(\r\x12\x1b\n\x13\x61uth0_users_updated\x18\x04 \x01(\r\x12\x1a\n\x12\x61uth0_orgs_deleted\x18\x05 \x01(\r\x12\x0e\n\x06\x65rrors\x18\x06 \x01(\r\x12$\n\x1c\x61\x63\x63ounts_without_auth0_match\x18\x07 \x01(\r\x12\x41\n\x06result\x18\n \x03(\x0b\x32\x31.api.MigratePersonalLegacyAccountsResponse.Result\x1a\xd3\x01\n\x06Result\x12\"\n\naccount_id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\x12\x15\n\rauth0_user_id\x18\x02 \x01(\t\x12\x14\n\x0c\x61uth0_org_id\x18\x03 \x01(\t\x12\x16\n\x0erecord_updated\x18\x04 \x01(\x08\x12\x1a\n\x12\x61uth0_user_updated\x18\x05 \x01(\x08\x12\x19\n\x11\x61uth0_org_deleted\x18\x06 \x01(\x08\x12\x12\n\nerror_code\x18\n \x01(\t\x12\x15\n\rerror_message\x18\x0b \x01(\t2\x82\x0e\n\nAccountAPI\x12[\n\x14GetAccountViewByName\x12 .api.GetAccountViewByNameRequest\x1a!.api.GetAccountViewByNameResponse\x12U\n\x12GetAccountViewById\x12\x1e.api.GetAccountViewByIdRequest\x1a\x1f.api.GetAccountViewByIdResponse\x12O\n\x10GetAccountByName\x12\x1c.api.GetAccountByNameRequest\x1a\x1d.api.GetAccountByNameResponse\x12I\n\x0eGetAccountById\x12\x1a.api.GetAccountByIdRequest\x1a\x1b.api.GetAccountByIdResponse\x12O\n\x10GetMyAccountView\x12\x1c.api.GetMyAccountViewRequest\x1a\x1d.api.GetMyAccountViewResponse\x12\x46\n\rCreateAccount\x12\x19.api.CreateAccountRequest\x1a\x1a.api.CreateAccountResponse\x12\x46\n\rUpdateAccount\x12\x19.api.UpdateAccountRequest\x1a\x1a.api.UpdateAccountResponse\x12j\n\x19\x43reateOrganizationAccount\x12%.api.CreateOrganizationAccountRequest\x1a&.api.CreateOrganizationAccountResponse\x12\x43\n\x0c\x43reateApiKey\x12\x18.api.CreateApiKeyRequest\x1a\x19.api.CreateApiKeyResponse\x12s\n\x1cToggleDatasetLikeByMyAccount\x12(.api.ToggleDatasetLikeByMyAccountRequest\x1a).api.ToggleDatasetLikeByMyAccountResponse\x12m\n\x1aGetDatasetLikedByMyAccount\x12&.api.GetDatasetLikedByMyAccountRequest\x1a\'.api.GetDatasetLikedByMyAccountResponse\x12m\n\x1aToggleModelLikeByMyAccount\x12&.api.ToggleModelLikeByMyAccountRequest\x1a\'.api.ToggleModelLikeByMyAccountResponse\x12g\n\x18GetModelLikedByMyAccount\x12$.api.GetModelLikedByMyAccountRequest\x1a%.api.GetModelLikedByMyAccountResponse\x12s\n\x1cToggleProjectLikeByMyAccount\x12(.api.ToggleProjectLikeByMyAccountRequest\x1a).api.ToggleProjectLikeByMyAccountResponse\x12m\n\x1aGetProjectLikedByMyAccount\x12&.api.GetProjectLikedByMyAccountRequest\x1a\'.api.GetProjectLikedByMyAccountResponse\x12g\n\x18GetTierConfigByAccountId\x12$.api.GetTierConfigByAccountIdRequest\x1a%.api.GetTierConfigByAccountIdResponse\x12X\n\x13\x41ssignTierToAccount\x12\x1f.api.AssignTierToAccountRequest\x1a .api.AssignTierToAccountResponse\x12\x37\n\x08GetTiers\x12\x14.api.GetTiersRequest\x1a\x15.api.GetTiersResponse\x12v\n\x1dMigratePersonalLegacyAccounts\x12).api.MigratePersonalLegacyAccountsRequest\x1a*.api.MigratePersonalLegacyAccountsResponseB\"\n\rcom.layer.apiB\x0f\x41\x63\x63ountApiProtoP\x01\x62\x06proto3')



_GETACCOUNTVIEWBYNAMEREQUEST = DESCRIPTOR.message_types_by_name['GetAccountViewByNameRequest']
_GETACCOUNTVIEWBYNAMERESPONSE = DESCRIPTOR.message_types_by_name['GetAccountViewByNameResponse']
_GETACCOUNTVIEWBYIDREQUEST = DESCRIPTOR.message_types_by_name['GetAccountViewByIdRequest']
_GETACCOUNTVIEWBYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetAccountViewByIdResponse']
_GETMYACCOUNTVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetMyAccountViewRequest']
_GETMYACCOUNTVIEWRESPONSE = DESCRIPTOR.message_types_by_name['GetMyAccountViewResponse']
_CREATEACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['CreateAccountRequest']
_CREATEACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['CreateAccountResponse']
_CREATEORGANIZATIONACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['CreateOrganizationAccountRequest']
_CREATEORGANIZATIONACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['CreateOrganizationAccountResponse']
_TOGGLEDATASETLIKEBYMYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['ToggleDatasetLikeByMyAccountRequest']
_TOGGLEDATASETLIKEBYMYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['ToggleDatasetLikeByMyAccountResponse']
_GETDATASETLIKEDBYMYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetLikedByMyAccountRequest']
_GETDATASETLIKEDBYMYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetLikedByMyAccountResponse']
_TOGGLEMODELLIKEBYMYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['ToggleModelLikeByMyAccountRequest']
_TOGGLEMODELLIKEBYMYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['ToggleModelLikeByMyAccountResponse']
_GETMODELLIKEDBYMYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetModelLikedByMyAccountRequest']
_GETMODELLIKEDBYMYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['GetModelLikedByMyAccountResponse']
_TOGGLEPROJECTLIKEBYMYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['ToggleProjectLikeByMyAccountRequest']
_TOGGLEPROJECTLIKEBYMYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['ToggleProjectLikeByMyAccountResponse']
_GETPROJECTLIKEDBYMYACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['GetProjectLikedByMyAccountRequest']
_GETPROJECTLIKEDBYMYACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['GetProjectLikedByMyAccountResponse']
_CREATEAPIKEYREQUEST = DESCRIPTOR.message_types_by_name['CreateApiKeyRequest']
_CREATEAPIKEYRESPONSE = DESCRIPTOR.message_types_by_name['CreateApiKeyResponse']
_GETTIERCONFIGBYACCOUNTIDREQUEST = DESCRIPTOR.message_types_by_name['GetTierConfigByAccountIdRequest']
_GETTIERCONFIGBYACCOUNTIDRESPONSE = DESCRIPTOR.message_types_by_name['GetTierConfigByAccountIdResponse']
_UPDATEACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['UpdateAccountRequest']
_UPDATEACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateAccountResponse']
_GETACCOUNTBYIDREQUEST = DESCRIPTOR.message_types_by_name['GetAccountByIdRequest']
_GETACCOUNTBYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetAccountByIdResponse']
_GETACCOUNTBYNAMEREQUEST = DESCRIPTOR.message_types_by_name['GetAccountByNameRequest']
_GETACCOUNTBYNAMERESPONSE = DESCRIPTOR.message_types_by_name['GetAccountByNameResponse']
_ASSIGNTIERTOACCOUNTREQUEST = DESCRIPTOR.message_types_by_name['AssignTierToAccountRequest']
_ASSIGNTIERTOACCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['AssignTierToAccountResponse']
_GETTIERSREQUEST = DESCRIPTOR.message_types_by_name['GetTiersRequest']
_GETTIERSRESPONSE = DESCRIPTOR.message_types_by_name['GetTiersResponse']
_MIGRATEPERSONALLEGACYACCOUNTSREQUEST = DESCRIPTOR.message_types_by_name['MigratePersonalLegacyAccountsRequest']
_MIGRATEPERSONALLEGACYACCOUNTSRESPONSE = DESCRIPTOR.message_types_by_name['MigratePersonalLegacyAccountsResponse']
_MIGRATEPERSONALLEGACYACCOUNTSRESPONSE_RESULT = _MIGRATEPERSONALLEGACYACCOUNTSRESPONSE.nested_types_by_name['Result']
GetAccountViewByNameRequest = _reflection.GeneratedProtocolMessageType('GetAccountViewByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTVIEWBYNAMEREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountViewByNameRequest)
  })
_sym_db.RegisterMessage(GetAccountViewByNameRequest)

GetAccountViewByNameResponse = _reflection.GeneratedProtocolMessageType('GetAccountViewByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTVIEWBYNAMERESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountViewByNameResponse)
  })
_sym_db.RegisterMessage(GetAccountViewByNameResponse)

GetAccountViewByIdRequest = _reflection.GeneratedProtocolMessageType('GetAccountViewByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTVIEWBYIDREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountViewByIdRequest)
  })
_sym_db.RegisterMessage(GetAccountViewByIdRequest)

GetAccountViewByIdResponse = _reflection.GeneratedProtocolMessageType('GetAccountViewByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTVIEWBYIDRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountViewByIdResponse)
  })
_sym_db.RegisterMessage(GetAccountViewByIdResponse)

GetMyAccountViewRequest = _reflection.GeneratedProtocolMessageType('GetMyAccountViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMYACCOUNTVIEWREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyAccountViewRequest)
  })
_sym_db.RegisterMessage(GetMyAccountViewRequest)

GetMyAccountViewResponse = _reflection.GeneratedProtocolMessageType('GetMyAccountViewResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMYACCOUNTVIEWRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyAccountViewResponse)
  })
_sym_db.RegisterMessage(GetMyAccountViewResponse)

CreateAccountRequest = _reflection.GeneratedProtocolMessageType('CreateAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateAccountRequest)
  })
_sym_db.RegisterMessage(CreateAccountRequest)

CreateAccountResponse = _reflection.GeneratedProtocolMessageType('CreateAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateAccountResponse)
  })
_sym_db.RegisterMessage(CreateAccountResponse)

CreateOrganizationAccountRequest = _reflection.GeneratedProtocolMessageType('CreateOrganizationAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGANIZATIONACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateOrganizationAccountRequest)
  })
_sym_db.RegisterMessage(CreateOrganizationAccountRequest)

CreateOrganizationAccountResponse = _reflection.GeneratedProtocolMessageType('CreateOrganizationAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGANIZATIONACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateOrganizationAccountResponse)
  })
_sym_db.RegisterMessage(CreateOrganizationAccountResponse)

ToggleDatasetLikeByMyAccountRequest = _reflection.GeneratedProtocolMessageType('ToggleDatasetLikeByMyAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEDATASETLIKEBYMYACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleDatasetLikeByMyAccountRequest)
  })
_sym_db.RegisterMessage(ToggleDatasetLikeByMyAccountRequest)

ToggleDatasetLikeByMyAccountResponse = _reflection.GeneratedProtocolMessageType('ToggleDatasetLikeByMyAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEDATASETLIKEBYMYACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleDatasetLikeByMyAccountResponse)
  })
_sym_db.RegisterMessage(ToggleDatasetLikeByMyAccountResponse)

GetDatasetLikedByMyAccountRequest = _reflection.GeneratedProtocolMessageType('GetDatasetLikedByMyAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETLIKEDBYMYACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetDatasetLikedByMyAccountRequest)
  })
_sym_db.RegisterMessage(GetDatasetLikedByMyAccountRequest)

GetDatasetLikedByMyAccountResponse = _reflection.GeneratedProtocolMessageType('GetDatasetLikedByMyAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETLIKEDBYMYACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetDatasetLikedByMyAccountResponse)
  })
_sym_db.RegisterMessage(GetDatasetLikedByMyAccountResponse)

ToggleModelLikeByMyAccountRequest = _reflection.GeneratedProtocolMessageType('ToggleModelLikeByMyAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEMODELLIKEBYMYACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleModelLikeByMyAccountRequest)
  })
_sym_db.RegisterMessage(ToggleModelLikeByMyAccountRequest)

ToggleModelLikeByMyAccountResponse = _reflection.GeneratedProtocolMessageType('ToggleModelLikeByMyAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEMODELLIKEBYMYACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleModelLikeByMyAccountResponse)
  })
_sym_db.RegisterMessage(ToggleModelLikeByMyAccountResponse)

GetModelLikedByMyAccountRequest = _reflection.GeneratedProtocolMessageType('GetModelLikedByMyAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELLIKEDBYMYACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetModelLikedByMyAccountRequest)
  })
_sym_db.RegisterMessage(GetModelLikedByMyAccountRequest)

GetModelLikedByMyAccountResponse = _reflection.GeneratedProtocolMessageType('GetModelLikedByMyAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELLIKEDBYMYACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetModelLikedByMyAccountResponse)
  })
_sym_db.RegisterMessage(GetModelLikedByMyAccountResponse)

ToggleProjectLikeByMyAccountRequest = _reflection.GeneratedProtocolMessageType('ToggleProjectLikeByMyAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEPROJECTLIKEBYMYACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleProjectLikeByMyAccountRequest)
  })
_sym_db.RegisterMessage(ToggleProjectLikeByMyAccountRequest)

ToggleProjectLikeByMyAccountResponse = _reflection.GeneratedProtocolMessageType('ToggleProjectLikeByMyAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEPROJECTLIKEBYMYACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleProjectLikeByMyAccountResponse)
  })
_sym_db.RegisterMessage(ToggleProjectLikeByMyAccountResponse)

GetProjectLikedByMyAccountRequest = _reflection.GeneratedProtocolMessageType('GetProjectLikedByMyAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTLIKEDBYMYACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetProjectLikedByMyAccountRequest)
  })
_sym_db.RegisterMessage(GetProjectLikedByMyAccountRequest)

GetProjectLikedByMyAccountResponse = _reflection.GeneratedProtocolMessageType('GetProjectLikedByMyAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTLIKEDBYMYACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetProjectLikedByMyAccountResponse)
  })
_sym_db.RegisterMessage(GetProjectLikedByMyAccountResponse)

CreateApiKeyRequest = _reflection.GeneratedProtocolMessageType('CreateApiKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAPIKEYREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateApiKeyRequest)
  })
_sym_db.RegisterMessage(CreateApiKeyRequest)

CreateApiKeyResponse = _reflection.GeneratedProtocolMessageType('CreateApiKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAPIKEYRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateApiKeyResponse)
  })
_sym_db.RegisterMessage(CreateApiKeyResponse)

GetTierConfigByAccountIdRequest = _reflection.GeneratedProtocolMessageType('GetTierConfigByAccountIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTIERCONFIGBYACCOUNTIDREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetTierConfigByAccountIdRequest)
  })
_sym_db.RegisterMessage(GetTierConfigByAccountIdRequest)

GetTierConfigByAccountIdResponse = _reflection.GeneratedProtocolMessageType('GetTierConfigByAccountIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTIERCONFIGBYACCOUNTIDRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetTierConfigByAccountIdResponse)
  })
_sym_db.RegisterMessage(GetTierConfigByAccountIdResponse)

UpdateAccountRequest = _reflection.GeneratedProtocolMessageType('UpdateAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateAccountRequest)
  })
_sym_db.RegisterMessage(UpdateAccountRequest)

UpdateAccountResponse = _reflection.GeneratedProtocolMessageType('UpdateAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateAccountResponse)
  })
_sym_db.RegisterMessage(UpdateAccountResponse)

GetAccountByIdRequest = _reflection.GeneratedProtocolMessageType('GetAccountByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTBYIDREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountByIdRequest)
  })
_sym_db.RegisterMessage(GetAccountByIdRequest)

GetAccountByIdResponse = _reflection.GeneratedProtocolMessageType('GetAccountByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTBYIDRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountByIdResponse)
  })
_sym_db.RegisterMessage(GetAccountByIdResponse)

GetAccountByNameRequest = _reflection.GeneratedProtocolMessageType('GetAccountByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTBYNAMEREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountByNameRequest)
  })
_sym_db.RegisterMessage(GetAccountByNameRequest)

GetAccountByNameResponse = _reflection.GeneratedProtocolMessageType('GetAccountByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTBYNAMERESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetAccountByNameResponse)
  })
_sym_db.RegisterMessage(GetAccountByNameResponse)

AssignTierToAccountRequest = _reflection.GeneratedProtocolMessageType('AssignTierToAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNTIERTOACCOUNTREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.AssignTierToAccountRequest)
  })
_sym_db.RegisterMessage(AssignTierToAccountRequest)

AssignTierToAccountResponse = _reflection.GeneratedProtocolMessageType('AssignTierToAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNTIERTOACCOUNTRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.AssignTierToAccountResponse)
  })
_sym_db.RegisterMessage(AssignTierToAccountResponse)

GetTiersRequest = _reflection.GeneratedProtocolMessageType('GetTiersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTIERSREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetTiersRequest)
  })
_sym_db.RegisterMessage(GetTiersRequest)

GetTiersResponse = _reflection.GeneratedProtocolMessageType('GetTiersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTIERSRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetTiersResponse)
  })
_sym_db.RegisterMessage(GetTiersResponse)

MigratePersonalLegacyAccountsRequest = _reflection.GeneratedProtocolMessageType('MigratePersonalLegacyAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MIGRATEPERSONALLEGACYACCOUNTSREQUEST,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.MigratePersonalLegacyAccountsRequest)
  })
_sym_db.RegisterMessage(MigratePersonalLegacyAccountsRequest)

MigratePersonalLegacyAccountsResponse = _reflection.GeneratedProtocolMessageType('MigratePersonalLegacyAccountsResponse', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _MIGRATEPERSONALLEGACYACCOUNTSRESPONSE_RESULT,
    '__module__' : 'api.service.account.account_api_pb2'
    # @@protoc_insertion_point(class_scope:api.MigratePersonalLegacyAccountsResponse.Result)
    })
  ,
  'DESCRIPTOR' : _MIGRATEPERSONALLEGACYACCOUNTSRESPONSE,
  '__module__' : 'api.service.account.account_api_pb2'
  # @@protoc_insertion_point(class_scope:api.MigratePersonalLegacyAccountsResponse)
  })
_sym_db.RegisterMessage(MigratePersonalLegacyAccountsResponse)
_sym_db.RegisterMessage(MigratePersonalLegacyAccountsResponse.Result)

_ACCOUNTAPI = DESCRIPTOR.services_by_name['AccountAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiB\017AccountApiProtoP\001'
  _CREATEACCOUNTREQUEST.fields_by_name['name']._options = None
  _CREATEACCOUNTREQUEST.fields_by_name['name']._serialized_options = b'\372B\006r\004\020\003\0302'
  _CREATEACCOUNTREQUEST.fields_by_name['display_name']._options = None
  _CREATEACCOUNTREQUEST.fields_by_name['display_name']._serialized_options = b'\372B\007r\005\020\003\030\377\001'
  _CREATEORGANIZATIONACCOUNTREQUEST.fields_by_name['name']._options = None
  _CREATEORGANIZATIONACCOUNTREQUEST.fields_by_name['name']._serialized_options = b'\372B\006r\004\020\003\0302'
  _CREATEORGANIZATIONACCOUNTREQUEST.fields_by_name['display_name']._options = None
  _CREATEORGANIZATIONACCOUNTREQUEST.fields_by_name['display_name']._serialized_options = b'\372B\007r\005\020\003\030\377\001'
  _TOGGLEDATASETLIKEBYMYACCOUNTREQUEST.fields_by_name['dataset_id']._options = None
  _TOGGLEDATASETLIKEBYMYACCOUNTREQUEST.fields_by_name['dataset_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETDATASETLIKEDBYMYACCOUNTREQUEST.fields_by_name['dataset_id']._options = None
  _GETDATASETLIKEDBYMYACCOUNTREQUEST.fields_by_name['dataset_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _TOGGLEMODELLIKEBYMYACCOUNTREQUEST.fields_by_name['model_id']._options = None
  _TOGGLEMODELLIKEBYMYACCOUNTREQUEST.fields_by_name['model_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETMODELLIKEDBYMYACCOUNTREQUEST.fields_by_name['model_id']._options = None
  _GETMODELLIKEDBYMYACCOUNTREQUEST.fields_by_name['model_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _TOGGLEPROJECTLIKEBYMYACCOUNTREQUEST.fields_by_name['project_id']._options = None
  _TOGGLEPROJECTLIKEBYMYACCOUNTREQUEST.fields_by_name['project_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETPROJECTLIKEDBYMYACCOUNTREQUEST.fields_by_name['project_id']._options = None
  _GETPROJECTLIKEDBYMYACCOUNTREQUEST.fields_by_name['project_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETTIERCONFIGBYACCOUNTIDREQUEST.fields_by_name['account_id']._options = None
  _GETTIERCONFIGBYACCOUNTIDREQUEST.fields_by_name['account_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _UPDATEACCOUNTREQUEST.fields_by_name['account_id']._options = None
  _UPDATEACCOUNTREQUEST.fields_by_name['account_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _UPDATEACCOUNTRESPONSE.fields_by_name['account_id']._options = None
  _UPDATEACCOUNTRESPONSE.fields_by_name['account_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETACCOUNTBYIDREQUEST.fields_by_name['account_id']._options = None
  _GETACCOUNTBYIDREQUEST.fields_by_name['account_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETACCOUNTBYIDRESPONSE.fields_by_name['account']._options = None
  _GETACCOUNTBYIDRESPONSE.fields_by_name['account']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETACCOUNTBYNAMEREQUEST.fields_by_name['name']._options = None
  _GETACCOUNTBYNAMEREQUEST.fields_by_name['name']._serialized_options = b'\372B\006r\004\020\003\0302'
  _GETACCOUNTBYNAMERESPONSE.fields_by_name['account']._options = None
  _GETACCOUNTBYNAMERESPONSE.fields_by_name['account']._serialized_options = b'\372B\005\212\001\002\020\001'
  _ASSIGNTIERTOACCOUNTREQUEST.fields_by_name['account_id']._options = None
  _ASSIGNTIERTOACCOUNTREQUEST.fields_by_name['account_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _ASSIGNTIERTOACCOUNTREQUEST.fields_by_name['tier_id']._options = None
  _ASSIGNTIERTOACCOUNTREQUEST.fields_by_name['tier_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETACCOUNTVIEWBYNAMEREQUEST._serialized_start=251
  _GETACCOUNTVIEWBYNAMEREQUEST._serialized_end=294
  _GETACCOUNTVIEWBYNAMERESPONSE._serialized_start=296
  _GETACCOUNTVIEWBYNAMERESPONSE._serialized_end=366
  _GETACCOUNTVIEWBYIDREQUEST._serialized_start=368
  _GETACCOUNTVIEWBYIDREQUEST._serialized_end=423
  _GETACCOUNTVIEWBYIDRESPONSE._serialized_start=425
  _GETACCOUNTVIEWBYIDRESPONSE._serialized_end=493
  _GETMYACCOUNTVIEWREQUEST._serialized_start=495
  _GETMYACCOUNTVIEWREQUEST._serialized_end=520
  _GETMYACCOUNTVIEWRESPONSE._serialized_start=522
  _GETMYACCOUNTVIEWRESPONSE._serialized_end=588
  _CREATEACCOUNTREQUEST._serialized_start=590
  _CREATEACCOUNTREQUEST._serialized_end=707
  _CREATEACCOUNTRESPONSE._serialized_start=709
  _CREATEACCOUNTRESPONSE._serialized_end=772
  _CREATEORGANIZATIONACCOUNTREQUEST._serialized_start=775
  _CREATEORGANIZATIONACCOUNTREQUEST._serialized_end=904
  _CREATEORGANIZATIONACCOUNTRESPONSE._serialized_start=906
  _CREATEORGANIZATIONACCOUNTRESPONSE._serialized_end=981
  _TOGGLEDATASETLIKEBYMYACCOUNTREQUEST._serialized_start=983
  _TOGGLEDATASETLIKEBYMYACCOUNTREQUEST._serialized_end=1066
  _TOGGLEDATASETLIKEBYMYACCOUNTRESPONSE._serialized_start=1068
  _TOGGLEDATASETLIKEBYMYACCOUNTRESPONSE._serialized_end=1124
  _GETDATASETLIKEDBYMYACCOUNTREQUEST._serialized_start=1126
  _GETDATASETLIKEDBYMYACCOUNTREQUEST._serialized_end=1207
  _GETDATASETLIKEDBYMYACCOUNTRESPONSE._serialized_start=1209
  _GETDATASETLIKEDBYMYACCOUNTRESPONSE._serialized_end=1263
  _TOGGLEMODELLIKEBYMYACCOUNTREQUEST._serialized_start=1265
  _TOGGLEMODELLIKEBYMYACCOUNTREQUEST._serialized_end=1342
  _TOGGLEMODELLIKEBYMYACCOUNTRESPONSE._serialized_start=1344
  _TOGGLEMODELLIKEBYMYACCOUNTRESPONSE._serialized_end=1398
  _GETMODELLIKEDBYMYACCOUNTREQUEST._serialized_start=1400
  _GETMODELLIKEDBYMYACCOUNTREQUEST._serialized_end=1475
  _GETMODELLIKEDBYMYACCOUNTRESPONSE._serialized_start=1477
  _GETMODELLIKEDBYMYACCOUNTRESPONSE._serialized_end=1529
  _TOGGLEPROJECTLIKEBYMYACCOUNTREQUEST._serialized_start=1531
  _TOGGLEPROJECTLIKEBYMYACCOUNTREQUEST._serialized_end=1614
  _TOGGLEPROJECTLIKEBYMYACCOUNTRESPONSE._serialized_start=1616
  _TOGGLEPROJECTLIKEBYMYACCOUNTRESPONSE._serialized_end=1672
  _GETPROJECTLIKEDBYMYACCOUNTREQUEST._serialized_start=1674
  _GETPROJECTLIKEDBYMYACCOUNTREQUEST._serialized_end=1755
  _GETPROJECTLIKEDBYMYACCOUNTRESPONSE._serialized_start=1757
  _GETPROJECTLIKEDBYMYACCOUNTRESPONSE._serialized_end=1811
  _CREATEAPIKEYREQUEST._serialized_start=1813
  _CREATEAPIKEYREQUEST._serialized_end=1870
  _CREATEAPIKEYRESPONSE._serialized_start=1872
  _CREATEAPIKEYRESPONSE._serialized_end=1911
  _GETTIERCONFIGBYACCOUNTIDREQUEST._serialized_start=1913
  _GETTIERCONFIGBYACCOUNTIDREQUEST._serialized_end=1992
  _GETTIERCONFIGBYACCOUNTIDRESPONSE._serialized_start=1994
  _GETTIERCONFIGBYACCOUNTIDRESPONSE._serialized_end=2067
  _UPDATEACCOUNTREQUEST._serialized_start=2070
  _UPDATEACCOUNTREQUEST._serialized_end=2205
  _UPDATEACCOUNTRESPONSE._serialized_start=2207
  _UPDATEACCOUNTRESPONSE._serialized_end=2276
  _GETACCOUNTBYIDREQUEST._serialized_start=2278
  _GETACCOUNTBYIDREQUEST._serialized_end=2347
  _GETACCOUNTBYIDRESPONSE._serialized_start=2349
  _GETACCOUNTBYIDRESPONSE._serialized_end=2414
  _GETACCOUNTBYNAMEREQUEST._serialized_start=2416
  _GETACCOUNTBYNAMEREQUEST._serialized_end=2466
  _GETACCOUNTBYNAMERESPONSE._serialized_start=2468
  _GETACCOUNTBYNAMERESPONSE._serialized_end=2535
  _ASSIGNTIERTOACCOUNTREQUEST._serialized_start=2537
  _ASSIGNTIERTOACCOUNTREQUEST._serialized_end=2651
  _ASSIGNTIERTOACCOUNTRESPONSE._serialized_start=2653
  _ASSIGNTIERTOACCOUNTRESPONSE._serialized_end=2718
  _GETTIERSREQUEST._serialized_start=2720
  _GETTIERSREQUEST._serialized_end=2737
  _GETTIERSRESPONSE._serialized_start=2739
  _GETTIERSRESPONSE._serialized_end=2783
  _MIGRATEPERSONALLEGACYACCOUNTSREQUEST._serialized_start=2785
  _MIGRATEPERSONALLEGACYACCOUNTSREQUEST._serialized_end=2872
  _MIGRATEPERSONALLEGACYACCOUNTSRESPONSE._serialized_start=2875
  _MIGRATEPERSONALLEGACYACCOUNTSRESPONSE._serialized_end=3375
  _MIGRATEPERSONALLEGACYACCOUNTSRESPONSE_RESULT._serialized_start=3164
  _MIGRATEPERSONALLEGACYACCOUNTSRESPONSE_RESULT._serialized_end=3375
  _ACCOUNTAPI._serialized_start=3378
  _ACCOUNTAPI._serialized_end=5172
# @@protoc_insertion_point(module_scope)
