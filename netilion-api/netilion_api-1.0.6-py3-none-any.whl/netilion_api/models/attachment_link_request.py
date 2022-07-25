# coding: utf-8

"""
    Netilion API Documentation

    Welcome to the Netilion API Documentation, which provides interactive access and documentation to our REST API. Please visit our developer portal for further instructions and information: https://developer.netilion.endress.com/   # noqa: E501

    OpenAPI spec version: 01.00.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from netilion_api.configuration import Configuration


class AttachmentLinkRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'content_author': 'str',
        'content_version': 'str',
        'content_date': 'str',
        'content_type': 'str',
        'file_name': 'str',
        'remarks': 'str',
        'document': 'NestedID',
        'languages': 'str'
    }

    attribute_map = {
        'href': 'href',
        'content_author': 'content_author',
        'content_version': 'content_version',
        'content_date': 'content_date',
        'content_type': 'content_type',
        'file_name': 'file_name',
        'remarks': 'remarks',
        'document': 'document',
        'languages': 'languages'
    }

    def __init__(self, href=None, content_author=None, content_version=None, content_date=None, content_type=None, file_name=None, remarks=None, document=None, languages=None, _configuration=None):  # noqa: E501
        """AttachmentLinkRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._href = None
        self._content_author = None
        self._content_version = None
        self._content_date = None
        self._content_type = None
        self._file_name = None
        self._remarks = None
        self._document = None
        self._languages = None
        self.discriminator = None

        self.href = href
        if content_author is not None:
            self.content_author = content_author
        if content_version is not None:
            self.content_version = content_version
        if content_date is not None:
            self.content_date = content_date
        if content_type is not None:
            self.content_type = content_type
        if file_name is not None:
            self.file_name = file_name
        if remarks is not None:
            self.remarks = remarks
        self.document = document
        if languages is not None:
            self.languages = languages

    @property
    def href(self):
        """Gets the href of this AttachmentLinkRequest.  # noqa: E501

        the link, must be http or https link  # noqa: E501

        :return: The href of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AttachmentLinkRequest.

        the link, must be http or https link  # noqa: E501

        :param href: The href of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def content_author(self):
        """Gets the content_author of this AttachmentLinkRequest.  # noqa: E501

        the file authors name  # noqa: E501

        :return: The content_author of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_author

    @content_author.setter
    def content_author(self, content_author):
        """Sets the content_author of this AttachmentLinkRequest.

        the file authors name  # noqa: E501

        :param content_author: The content_author of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """

        self._content_author = content_author

    @property
    def content_version(self):
        """Gets the content_version of this AttachmentLinkRequest.  # noqa: E501

        the version of the attachment  # noqa: E501

        :return: The content_version of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_version

    @content_version.setter
    def content_version(self, content_version):
        """Sets the content_version of this AttachmentLinkRequest.

        the version of the attachment  # noqa: E501

        :param content_version: The content_version of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """

        self._content_version = content_version

    @property
    def content_date(self):
        """Gets the content_date of this AttachmentLinkRequest.  # noqa: E501

        last edit date of the file  # noqa: E501

        :return: The content_date of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_date

    @content_date.setter
    def content_date(self, content_date):
        """Sets the content_date of this AttachmentLinkRequest.

        last edit date of the file  # noqa: E501

        :param content_date: The content_date of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """

        self._content_date = content_date

    @property
    def content_type(self):
        """Gets the content_type of this AttachmentLinkRequest.  # noqa: E501

        content type of the file  # noqa: E501

        :return: The content_type of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this AttachmentLinkRequest.

        content type of the file  # noqa: E501

        :param content_type: The content_type of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def file_name(self):
        """Gets the file_name of this AttachmentLinkRequest.  # noqa: E501

        the name of the file  # noqa: E501

        :return: The file_name of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AttachmentLinkRequest.

        the name of the file  # noqa: E501

        :param file_name: The file_name of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def remarks(self):
        """Gets the remarks of this AttachmentLinkRequest.  # noqa: E501

        remarks of the attachment  # noqa: E501

        :return: The remarks of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this AttachmentLinkRequest.

        remarks of the attachment  # noqa: E501

        :param remarks: The remarks of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """

        self._remarks = remarks

    @property
    def document(self):
        """Gets the document of this AttachmentLinkRequest.  # noqa: E501


        :return: The document of this AttachmentLinkRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this AttachmentLinkRequest.


        :param document: The document of this AttachmentLinkRequest.  # noqa: E501
        :type: NestedID
        """
        if self._configuration.client_side_validation and document is None:
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def languages(self):
        """Gets the languages of this AttachmentLinkRequest.  # noqa: E501

        the languages of the files content  # noqa: E501

        :return: The languages of this AttachmentLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this AttachmentLinkRequest.

        the languages of the files content  # noqa: E501

        :param languages: The languages of this AttachmentLinkRequest.  # noqa: E501
        :type: str
        """

        self._languages = languages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AttachmentLinkRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AttachmentLinkRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentLinkRequest):
            return True

        return self.to_dict() != other.to_dict()
