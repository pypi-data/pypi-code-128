""" Unit Test Data Structure Element
"""
from unittest.case import TestCase
from unittest.mock import Mock

from bson import ObjectId
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from mock import patch

import core_parser_app.components.data_structure_element.api as data_structure_element_api
from core_main_app.commons import exceptions
from core_main_app.utils.tests_tools.MockUser import create_mock_user
from core_parser_app.components.data_structure_element.models import (
    DataStructureElement,
)
from tests.components.data_structure_element.fixtures.fixtures import (
    DataStructureElementFixtures,
)
from tests.fixtures_utils import MockDataStructure


class TestDataStructureElementGetById(TestCase):
    def setUp(self):
        self.fixtures = DataStructureElementFixtures()
        self.fixtures.insert_data(user=self.fixtures.default_owner_with_perm)

        self.users = {
            "anon": AnonymousUser(),
            "user": self.fixtures.other_user_with_perm,
            "owner": self.fixtures.default_owner_with_perm,
            "superuser": self.fixtures.superuser,
        }

        self.mock_data_structure_element = DataStructureElement(
            id=ObjectId(),
            user=str(self.users["owner"].id),
            tag="mock_tag",
            value="mock_value",
            data_structure=self.fixtures.data_structure,
        )

        self.mock_request = Mock(spec=HttpRequest)

    @patch.object(DataStructureElement, "get_by_id_and_user")
    def test_data_structure_element_get_by_id_raises_does_not_exist_error_if_not_found(
        self, mock_get
    ):
        # Arrange
        mock_get.side_effect = exceptions.DoesNotExist("")
        self.mock_request.user = self.users["user"]
        # Act # Assert
        with self.assertRaises(exceptions.DoesNotExist):
            data_structure_element_api.get_by_id(1, self.mock_request)

    def test_data_structure_element_get_by_id_raises_model_error_if_not_found(self):
        self.mock_request.user = self.users["user"]

        # Act # Assert
        with self.assertRaises(exceptions.ModelError):
            data_structure_element_api.get_by_id(1, self.mock_request)

    @patch.object(DataStructureElement, "get_by_id_and_user")
    def test_data_structure_element_get_by_id_return_data_if_found(self, mock_get):
        # Arrange
        mock_get.return_value = self.mock_data_structure_element

        self.mock_request.user = self.users["owner"]
        # Act
        result = data_structure_element_api.get_by_id(1, self.mock_request)
        # Assert
        self.assertIsInstance(result, DataStructureElement)


class TestDataStructureElementGetByXpath(TestCase):
    @patch.object(DataStructureElement, "get_by_xpath_and_user")
    def test_data_structure_element_get_by_xpath_raises_does_not_exist_error_if_not_found(
        self, mock_get
    ):
        # Arrange
        mock_request = Mock(spec=HttpRequest)
        mock_request.user = create_mock_user("1")

        mock_get.side_effect = exceptions.DoesNotExist("")
        # Act # Assert
        with self.assertRaises(exceptions.DoesNotExist):
            data_structure_element_api.get_by_xpath("value_xpath", mock_request)

    @patch.object(DataStructureElement, "get_by_xpath")
    def test_data_structure_element_get_by_xpath_return_data_if_found(self, mock_get):
        # Arrange
        mock_data_structure_element = DataStructureElement(
            tag="tag", value="value", options={"xpath.xml": "value_xpath"}
        )
        mock_get.return_value = mock_data_structure_element
        # Act
        result = DataStructureElement.get_by_xpath("value_xpath")
        # Assert
        self.assertEqual(result, mock_data_structure_element)


class TestDataStructureElementGetAllByChildId(TestCase):
    def setUp(self):
        self.fixtures = DataStructureElementFixtures()
        self.fixtures.insert_data(user=self.fixtures.default_owner_with_perm)

        self.users = {
            "anon": AnonymousUser(),
            "user": self.fixtures.other_user_with_perm,
            "owner": self.fixtures.default_owner_with_perm,
            "superuser": self.fixtures.superuser,
        }

        self.mock_data_structure_element = DataStructureElement(
            id=ObjectId(),
            user=str(self.users["owner"].id),
            tag="mock_tag",
            value="mock_value",
            data_structure=self.fixtures.data_structure,
        )

        self.mock_request = Mock(spec=HttpRequest)

    def test_data_structure_element_get_by_id_raises_model_error_if_not_found(self):
        self.mock_request.user = self.users["user"]

        # Act # Assert
        with self.assertRaises(exceptions.ModelError):
            data_structure_element_api.get_all_by_child_id(1, self.mock_request)

    @patch.object(DataStructureElement, "get_all_by_child_id_and_user")
    def test_data_structure_element_get_all_by_id_return_data_if_found(self, mock_get):
        # Arrange
        mock_get.return_value = [self.mock_data_structure_element]
        self.mock_request.user = self.users["owner"]
        # Act
        result = data_structure_element_api.get_all_by_child_id(1, self.mock_request)
        # Assert
        self.assertTrue(all(isinstance(item, DataStructureElement) for item in result))


class TestDataStructureElementUpsert(TestCase):
    @patch.object(DataStructureElement, "save")
    def test_data_structure_element_upsert_return_data_structure_element(
        self, mock_save
    ):
        # Arrange
        mock_user = create_mock_user("1", is_superuser=True)
        mock_request = Mock(spec=HttpRequest)
        mock_request.user = mock_user

        mock_data_structure_element = DataStructureElement(
            user="1", tag="tag", value="value", data_structure=MockDataStructure()
        )
        mock_save.return_value = mock_data_structure_element

        # Act
        result = data_structure_element_api.upsert(
            mock_data_structure_element, mock_request
        )

        # Assert
        self.assertIsInstance(result, DataStructureElement)
