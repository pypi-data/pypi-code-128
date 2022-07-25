from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_flows_response_200_item_value_modules_item_input_transform import (
    ListFlowsResponse200ItemValueModulesItemInputTransform,
)
from ..models.list_flows_response_200_item_value_modules_item_value import ListFlowsResponse200ItemValueModulesItemValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListFlowsResponse200ItemValueModulesItem")


@attr.s(auto_attribs=True)
class ListFlowsResponse200ItemValueModulesItem:
    """ """

    input_transform: ListFlowsResponse200ItemValueModulesItemInputTransform
    value: ListFlowsResponse200ItemValueModulesItemValue
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
        input_transform = ListFlowsResponse200ItemValueModulesItemInputTransform.from_dict(d.pop("input_transform"))

        value = ListFlowsResponse200ItemValueModulesItemValue.from_dict(d.pop("value"))

        stop_after_if_expr = d.pop("stop_after_if_expr", UNSET)

        skip_if_stopped = d.pop("skip_if_stopped", UNSET)

        list_flows_response_200_item_value_modules_item = cls(
            input_transform=input_transform,
            value=value,
            stop_after_if_expr=stop_after_if_expr,
            skip_if_stopped=skip_if_stopped,
        )

        list_flows_response_200_item_value_modules_item.additional_properties = d
        return list_flows_response_200_item_value_modules_item

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
