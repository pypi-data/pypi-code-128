from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.flow_status_failure_module import FlowStatusFailureModule
from ..models.flow_status_modules_item import FlowStatusModulesItem

T = TypeVar("T", bound="FlowStatus")


@attr.s(auto_attribs=True)
class FlowStatus:
    """ """

    step: int
    modules: List[FlowStatusModulesItem]
    failure_module: FlowStatusFailureModule
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step = self.step
        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()

            modules.append(modules_item)

        failure_module = self.failure_module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "modules": modules,
                "failure_module": failure_module,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        step = d.pop("step")

        modules = []
        _modules = d.pop("modules")
        for modules_item_data in _modules:
            modules_item = FlowStatusModulesItem.from_dict(modules_item_data)

            modules.append(modules_item)

        failure_module = FlowStatusFailureModule.from_dict(d.pop("failure_module"))

        flow_status = cls(
            step=step,
            modules=modules,
            failure_module=failure_module,
        )

        flow_status.additional_properties = d
        return flow_status

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
