from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_completed_jobs_response_200_item_raw_flow_modules_item_input_transform import (
    ListCompletedJobsResponse200ItemRawFlowModulesItemInputTransform,
)
from ..models.list_completed_jobs_response_200_item_raw_flow_modules_item_value import (
    ListCompletedJobsResponse200ItemRawFlowModulesItemValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCompletedJobsResponse200ItemRawFlowModulesItem")


@attr.s(auto_attribs=True)
class ListCompletedJobsResponse200ItemRawFlowModulesItem:
    """ """

    input_transform: ListCompletedJobsResponse200ItemRawFlowModulesItemInputTransform
    value: ListCompletedJobsResponse200ItemRawFlowModulesItemValue
    stop_after_if_expr: Union[Unset, str] = UNSET
    skip_if_stopped: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_transform = self.input_transform.to_dict()

        value = self.value.to_dict()

        stop_after_if_expr = self.stop_after_if_expr
        skip_if_stopped = self.skip_if_stopped

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_transform": input_transform,
                "value": value,
            }
        )
        if stop_after_if_expr is not UNSET:
            field_dict["stop_after_if_expr"] = stop_after_if_expr
        if skip_if_stopped is not UNSET:
            field_dict["skip_if_stopped"] = skip_if_stopped

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_transform = ListCompletedJobsResponse200ItemRawFlowModulesItemInputTransform.from_dict(
            d.pop("input_transform")
        )

        value = ListCompletedJobsResponse200ItemRawFlowModulesItemValue.from_dict(d.pop("value"))

        stop_after_if_expr = d.pop("stop_after_if_expr", UNSET)

        skip_if_stopped = d.pop("skip_if_stopped", UNSET)

        list_completed_jobs_response_200_item_raw_flow_modules_item = cls(
            input_transform=input_transform,
            value=value,
            stop_after_if_expr=stop_after_if_expr,
            skip_if_stopped=skip_if_stopped,
        )

        list_completed_jobs_response_200_item_raw_flow_modules_item.additional_properties = d
        return list_completed_jobs_response_200_item_raw_flow_modules_item

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
