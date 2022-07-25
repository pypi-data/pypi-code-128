from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCompletedJobsResponse200ItemFlowStatusFailureModuleIterator")


@attr.s(auto_attribs=True)
class ListCompletedJobsResponse200ItemFlowStatusFailureModuleIterator:
    """ """

    index: Union[Unset, int] = UNSET
    itered: Union[Unset, List[None]] = UNSET
    args: Union[Unset, None] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        itered: Union[Unset, List[None]] = UNSET
        if not isinstance(self.itered, Unset):
            itered = []
            for itered_item_data in self.itered:
                itered_item = None

                itered.append(itered_item)

        args = None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if itered is not UNSET:
            field_dict["itered"] = itered
        if args is not UNSET:
            field_dict["args"] = args

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        itered = []
        _itered = d.pop("itered", UNSET)
        for itered_item_data in _itered or []:
            itered_item = None

            itered.append(itered_item)

        args = None

        list_completed_jobs_response_200_item_flow_status_failure_module_iterator = cls(
            index=index,
            itered=itered,
            args=args,
        )

        list_completed_jobs_response_200_item_flow_status_failure_module_iterator.additional_properties = d
        return list_completed_jobs_response_200_item_flow_status_failure_module_iterator

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
