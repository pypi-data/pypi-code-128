import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.flow_extra_perms import FlowExtraPerms
from ..models.flow_schema import FlowSchema
from ..models.flow_value import FlowValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="Flow")


@attr.s(auto_attribs=True)
class Flow:
    """ """

    path: str
    summary: str
    value: FlowValue
    edited_by: str
    edited_at: datetime.datetime
    archived: bool
    extra_perms: FlowExtraPerms
    workspace_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    schema: Union[Unset, FlowSchema] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        summary = self.summary
        value = self.value.to_dict()

        edited_by = self.edited_by
        edited_at = self.edited_at.isoformat()

        archived = self.archived
        extra_perms = self.extra_perms.to_dict()

        workspace_id = self.workspace_id
        description = self.description
        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "summary": summary,
                "value": value,
                "edited_by": edited_by,
                "edited_at": edited_at,
                "archived": archived,
                "extra_perms": extra_perms,
            }
        )
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if description is not UNSET:
            field_dict["description"] = description
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        summary = d.pop("summary")

        value = FlowValue.from_dict(d.pop("value"))

        edited_by = d.pop("edited_by")

        edited_at = isoparse(d.pop("edited_at"))

        archived = d.pop("archived")

        extra_perms = FlowExtraPerms.from_dict(d.pop("extra_perms"))

        workspace_id = d.pop("workspace_id", UNSET)

        description = d.pop("description", UNSET)

        schema: Union[Unset, FlowSchema] = UNSET
        _schema = d.pop("schema", UNSET)
        if not isinstance(_schema, Unset):
            schema = FlowSchema.from_dict(_schema)

        flow = cls(
            path=path,
            summary=summary,
            value=value,
            edited_by=edited_by,
            edited_at=edited_at,
            archived=archived,
            extra_perms=extra_perms,
            workspace_id=workspace_id,
            description=description,
            schema=schema,
        )

        flow.additional_properties = d
        return flow

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
