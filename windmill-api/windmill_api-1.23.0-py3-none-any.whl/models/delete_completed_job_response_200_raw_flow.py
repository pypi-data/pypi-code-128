from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.delete_completed_job_response_200_raw_flow_failure_module import (
    DeleteCompletedJobResponse200RawFlowFailureModule,
)
from ..models.delete_completed_job_response_200_raw_flow_modules_item import (
    DeleteCompletedJobResponse200RawFlowModulesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCompletedJobResponse200RawFlow")


@attr.s(auto_attribs=True)
class DeleteCompletedJobResponse200RawFlow:
    """ """

    modules: List[DeleteCompletedJobResponse200RawFlowModulesItem]
    failure_module: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModule] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()

            modules.append(modules_item)

        failure_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.failure_module, Unset):
            failure_module = self.failure_module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modules": modules,
            }
        )
        if failure_module is not UNSET:
            field_dict["failure_module"] = failure_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        modules = []
        _modules = d.pop("modules")
        for modules_item_data in _modules:
            modules_item = DeleteCompletedJobResponse200RawFlowModulesItem.from_dict(modules_item_data)

            modules.append(modules_item)

        failure_module: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModule] = UNSET
        _failure_module = d.pop("failure_module", UNSET)
        if not isinstance(_failure_module, Unset):
            failure_module = DeleteCompletedJobResponse200RawFlowFailureModule.from_dict(_failure_module)

        delete_completed_job_response_200_raw_flow = cls(
            modules=modules,
            failure_module=failure_module,
        )

        delete_completed_job_response_200_raw_flow.additional_properties = d
        return delete_completed_job_response_200_raw_flow

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
