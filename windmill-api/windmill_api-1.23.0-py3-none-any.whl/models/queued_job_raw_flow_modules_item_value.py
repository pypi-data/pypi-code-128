from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.queued_job_raw_flow_modules_item_value_iterator import QueuedJobRawFlowModulesItemValueIterator
from ..models.queued_job_raw_flow_modules_item_value_language import QueuedJobRawFlowModulesItemValueLanguage
from ..models.queued_job_raw_flow_modules_item_value_type import QueuedJobRawFlowModulesItemValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueuedJobRawFlowModulesItemValue")


@attr.s(auto_attribs=True)
class QueuedJobRawFlowModulesItemValue:
    """ """

    type: QueuedJobRawFlowModulesItemValueType
    iterator: Union[Unset, QueuedJobRawFlowModulesItemValueIterator] = UNSET
    path: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    language: Union[Unset, QueuedJobRawFlowModulesItemValueLanguage] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        iterator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iterator, Unset):
            iterator = self.iterator.to_dict()

        path = self.path
        content = self.content
        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if iterator is not UNSET:
            field_dict["iterator"] = iterator
        if path is not UNSET:
            field_dict["path"] = path
        if content is not UNSET:
            field_dict["content"] = content
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = QueuedJobRawFlowModulesItemValueType(d.pop("type"))

        iterator: Union[Unset, QueuedJobRawFlowModulesItemValueIterator] = UNSET
        _iterator = d.pop("iterator", UNSET)
        if not isinstance(_iterator, Unset):
            iterator = QueuedJobRawFlowModulesItemValueIterator.from_dict(_iterator)

        path = d.pop("path", UNSET)

        content = d.pop("content", UNSET)

        language: Union[Unset, QueuedJobRawFlowModulesItemValueLanguage] = UNSET
        _language = d.pop("language", UNSET)
        if not isinstance(_language, Unset):
            language = QueuedJobRawFlowModulesItemValueLanguage(_language)

        queued_job_raw_flow_modules_item_value = cls(
            type=type,
            iterator=iterator,
            path=path,
            content=content,
            language=language,
        )

        queued_job_raw_flow_modules_item_value.additional_properties = d
        return queued_job_raw_flow_modules_item_value

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
