from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.new_schedule_args import NewScheduleArgs
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewSchedule")


@attr.s(auto_attribs=True)
class NewSchedule:
    """ """

    path: str
    schedule: str
    script_path: str
    is_flow: bool
    args: NewScheduleArgs
    offset: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        schedule = self.schedule
        script_path = self.script_path
        is_flow = self.is_flow
        args = self.args.to_dict()

        offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "schedule": schedule,
                "script_path": script_path,
                "is_flow": is_flow,
                "args": args,
            }
        )
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        schedule = d.pop("schedule")

        script_path = d.pop("script_path")

        is_flow = d.pop("is_flow")

        args = NewScheduleArgs.from_dict(d.pop("args"))

        offset = d.pop("offset", UNSET)

        new_schedule = cls(
            path=path,
            schedule=schedule,
            script_path=script_path,
            is_flow=is_flow,
            args=args,
            offset=offset,
        )

        new_schedule.additional_properties = d
        return new_schedule

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
