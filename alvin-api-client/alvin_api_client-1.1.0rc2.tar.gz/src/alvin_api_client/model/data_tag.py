"""
    Alvin

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from alvin_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from alvin_api_client.exceptions import ApiAttributeError


def lazy_import():
    from alvin_api_client.model.data_tag_classification_type import DataTagClassificationType
    from alvin_api_client.model.data_tag_created_in import DataTagCreatedIn
    from alvin_api_client.model.data_tag_status import DataTagStatus
    from alvin_api_client.model.data_tag_type import DataTagType
    from alvin_api_client.model.tag_data_type import TagDataType
    globals()['DataTagClassificationType'] = DataTagClassificationType
    globals()['DataTagCreatedIn'] = DataTagCreatedIn
    globals()['DataTagStatus'] = DataTagStatus
    globals()['DataTagType'] = DataTagType
    globals()['TagDataType'] = TagDataType


class DataTag(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'name': (str,),  # noqa: E501
            'domain': (str,),  # noqa: E501
            'status': (DataTagStatus,),  # noqa: E501
            'type': (DataTagType,),  # noqa: E501
            'classification_type': (DataTagClassificationType,),  # noqa: E501
            'created_in': (DataTagCreatedIn,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'parent': (str,),  # noqa: E501
            'calculate_formula': (str,),  # noqa: E501
            'data_owner': ([str],),  # noqa: E501
            'data_steward': ([str],),  # noqa: E501
            'tag_data_type': (TagDataType,),  # noqa: E501
            'retention_time': (date,),  # noqa: E501
            'underage': (str,),  # noqa: E501
            'policy': (str,),  # noqa: E501
            'regulation': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'domain': 'domain',  # noqa: E501
        'status': 'status',  # noqa: E501
        'type': 'type',  # noqa: E501
        'classification_type': 'classificationType',  # noqa: E501
        'created_in': 'createdIn',  # noqa: E501
        'description': 'description',  # noqa: E501
        'parent': 'parent',  # noqa: E501
        'calculate_formula': 'calculateFormula',  # noqa: E501
        'data_owner': 'dataOwner',  # noqa: E501
        'data_steward': 'dataSteward',  # noqa: E501
        'tag_data_type': 'tagDataType',  # noqa: E501
        'retention_time': 'retentionTime',  # noqa: E501
        'underage': 'underage',  # noqa: E501
        'policy': 'policy',  # noqa: E501
        'regulation': 'regulation',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, domain, status, type, classification_type, created_in, *args, **kwargs):  # noqa: E501
        """DataTag - a model defined in OpenAPI

        Args:
            name (str):
            domain (str):
            status (DataTagStatus):
            type (DataTagType):
            classification_type (DataTagClassificationType):
            created_in (DataTagCreatedIn):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str): [optional]  # noqa: E501
            parent (str): [optional]  # noqa: E501
            calculate_formula (str): [optional]  # noqa: E501
            data_owner ([str]): [optional]  # noqa: E501
            data_steward ([str]): [optional]  # noqa: E501
            tag_data_type (TagDataType): [optional]  # noqa: E501
            retention_time (date): [optional]  # noqa: E501
            underage (str): [optional]  # noqa: E501
            policy (str): [optional]  # noqa: E501
            regulation (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        self.domain = domain
        self.status = status
        self.type = type
        self.classification_type = classification_type
        self.created_in = created_in
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, name, domain, status, type, classification_type, created_in, *args, **kwargs):  # noqa: E501
        """DataTag - a model defined in OpenAPI

        Args:
            name (str):
            domain (str):
            status (DataTagStatus):
            type (DataTagType):
            classification_type (DataTagClassificationType):
            created_in (DataTagCreatedIn):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            description (str): [optional]  # noqa: E501
            parent (str): [optional]  # noqa: E501
            calculate_formula (str): [optional]  # noqa: E501
            data_owner ([str]): [optional]  # noqa: E501
            data_steward ([str]): [optional]  # noqa: E501
            tag_data_type (TagDataType): [optional]  # noqa: E501
            retention_time (date): [optional]  # noqa: E501
            underage (str): [optional]  # noqa: E501
            policy (str): [optional]  # noqa: E501
            regulation (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        self.domain = domain
        self.status = status
        self.type = type
        self.classification_type = classification_type
        self.created_in = created_in
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
