import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.get_script_by_path_response_200_extra_perms import GetScriptByPathResponse200ExtraPerms
from ..models.get_script_by_path_response_200_language import GetScriptByPathResponse200Language
from ..models.get_script_by_path_response_200_schema import GetScriptByPathResponse200Schema
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScriptByPathResponse200")


@attr.s(auto_attribs=True)
class GetScriptByPathResponse200:
    """ """

    hash_: str
    path: str
    summary: str
    content: str
    created_by: str
    created_at: datetime.datetime
    archived: bool
    deleted: bool
    is_template: bool
    extra_perms: GetScriptByPathResponse200ExtraPerms
    language: GetScriptByPathResponse200Language
    is_trigger: bool
    workspace_id: Union[Unset, str] = UNSET
    parent_hashes: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    schema: Union[Unset, GetScriptByPathResponse200Schema] = UNSET
    lock: Union[Unset, str] = UNSET
    lock_error_logs: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hash_ = self.hash_
        path = self.path
        summary = self.summary
        content = self.content
        created_by = self.created_by
        created_at = self.created_at.isoformat()

        archived = self.archived
        deleted = self.deleted
        is_template = self.is_template
        extra_perms = self.extra_perms.to_dict()

        language = self.language.value

        is_trigger = self.is_trigger
        workspace_id = self.workspace_id
        parent_hashes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_hashes, Unset):
            parent_hashes = self.parent_hashes

        description = self.description
        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        lock = self.lock
        lock_error_logs = self.lock_error_logs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash": hash_,
                "path": path,
                "summary": summary,
                "content": content,
                "created_by": created_by,
                "created_at": created_at,
                "archived": archived,
                "deleted": deleted,
                "is_template": is_template,
                "extra_perms": extra_perms,
                "language": language,
                "is_trigger": is_trigger,
            }
        )
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if parent_hashes is not UNSET:
            field_dict["parent_hashes"] = parent_hashes
        if description is not UNSET:
            field_dict["description"] = description
        if schema is not UNSET:
            field_dict["schema"] = schema
        if lock is not UNSET:
            field_dict["lock"] = lock
        if lock_error_logs is not UNSET:
            field_dict["lock_error_logs"] = lock_error_logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hash_ = d.pop("hash")

        path = d.pop("path")

        summary = d.pop("summary")

        content = d.pop("content")

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        archived = d.pop("archived")

        deleted = d.pop("deleted")

        is_template = d.pop("is_template")

        extra_perms = GetScriptByPathResponse200ExtraPerms.from_dict(d.pop("extra_perms"))

        language = GetScriptByPathResponse200Language(d.pop("language"))

        is_trigger = d.pop("is_trigger")

        workspace_id = d.pop("workspace_id", UNSET)

        parent_hashes = cast(List[str], d.pop("parent_hashes", UNSET))

        description = d.pop("description", UNSET)

        schema: Union[Unset, GetScriptByPathResponse200Schema] = UNSET
        _schema = d.pop("schema", UNSET)
        if not isinstance(_schema, Unset):
            schema = GetScriptByPathResponse200Schema.from_dict(_schema)

        lock = d.pop("lock", UNSET)

        lock_error_logs = d.pop("lock_error_logs", UNSET)

        get_script_by_path_response_200 = cls(
            hash_=hash_,
            path=path,
            summary=summary,
            content=content,
            created_by=created_by,
            created_at=created_at,
            archived=archived,
            deleted=deleted,
            is_template=is_template,
            extra_perms=extra_perms,
            language=language,
            is_trigger=is_trigger,
            workspace_id=workspace_id,
            parent_hashes=parent_hashes,
            description=description,
            schema=schema,
            lock=lock,
            lock_error_logs=lock_error_logs,
        )

        get_script_by_path_response_200.additional_properties = d
        return get_script_by_path_response_200

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
