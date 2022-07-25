import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.get_completed_job_response_200_args import GetCompletedJobResponse200Args
from ..models.get_completed_job_response_200_flow_status import GetCompletedJobResponse200FlowStatus
from ..models.get_completed_job_response_200_job_kind import GetCompletedJobResponse200JobKind
from ..models.get_completed_job_response_200_language import GetCompletedJobResponse200Language
from ..models.get_completed_job_response_200_raw_flow import GetCompletedJobResponse200RawFlow
from ..models.get_completed_job_response_200_result import GetCompletedJobResponse200Result
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompletedJobResponse200")


@attr.s(auto_attribs=True)
class GetCompletedJobResponse200:
    """ """

    id: str
    created_by: str
    created_at: datetime.datetime
    started_at: datetime.datetime
    duration: int
    success: bool
    canceled: bool
    job_kind: GetCompletedJobResponse200JobKind
    permissioned_as: str
    is_flow_step: bool
    is_skipped: bool
    workspace_id: Union[Unset, str] = UNSET
    parent_job: Union[Unset, str] = UNSET
    script_path: Union[Unset, str] = UNSET
    script_hash: Union[Unset, str] = UNSET
    args: Union[Unset, GetCompletedJobResponse200Args] = UNSET
    result: Union[Unset, GetCompletedJobResponse200Result] = UNSET
    logs: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    raw_code: Union[Unset, str] = UNSET
    canceled_by: Union[Unset, str] = UNSET
    canceled_reason: Union[Unset, str] = UNSET
    schedule_path: Union[Unset, str] = UNSET
    flow_status: Union[Unset, GetCompletedJobResponse200FlowStatus] = UNSET
    raw_flow: Union[Unset, GetCompletedJobResponse200RawFlow] = UNSET
    language: Union[Unset, GetCompletedJobResponse200Language] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_by = self.created_by
        created_at = self.created_at.isoformat()

        started_at = self.started_at.isoformat()

        duration = self.duration
        success = self.success
        canceled = self.canceled
        job_kind = self.job_kind.value

        permissioned_as = self.permissioned_as
        is_flow_step = self.is_flow_step
        is_skipped = self.is_skipped
        workspace_id = self.workspace_id
        parent_job = self.parent_job
        script_path = self.script_path
        script_hash = self.script_hash
        args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        logs = self.logs
        deleted = self.deleted
        raw_code = self.raw_code
        canceled_by = self.canceled_by
        canceled_reason = self.canceled_reason
        schedule_path = self.schedule_path
        flow_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flow_status, Unset):
            flow_status = self.flow_status.to_dict()

        raw_flow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.raw_flow, Unset):
            raw_flow = self.raw_flow.to_dict()

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_by": created_by,
                "created_at": created_at,
                "started_at": started_at,
                "duration": duration,
                "success": success,
                "canceled": canceled,
                "job_kind": job_kind,
                "permissioned_as": permissioned_as,
                "is_flow_step": is_flow_step,
                "is_skipped": is_skipped,
            }
        )
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if parent_job is not UNSET:
            field_dict["parent_job"] = parent_job
        if script_path is not UNSET:
            field_dict["script_path"] = script_path
        if script_hash is not UNSET:
            field_dict["script_hash"] = script_hash
        if args is not UNSET:
            field_dict["args"] = args
        if result is not UNSET:
            field_dict["result"] = result
        if logs is not UNSET:
            field_dict["logs"] = logs
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if raw_code is not UNSET:
            field_dict["raw_code"] = raw_code
        if canceled_by is not UNSET:
            field_dict["canceled_by"] = canceled_by
        if canceled_reason is not UNSET:
            field_dict["canceled_reason"] = canceled_reason
        if schedule_path is not UNSET:
            field_dict["schedule_path"] = schedule_path
        if flow_status is not UNSET:
            field_dict["flow_status"] = flow_status
        if raw_flow is not UNSET:
            field_dict["raw_flow"] = raw_flow
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        started_at = isoparse(d.pop("started_at"))

        duration = d.pop("duration")

        success = d.pop("success")

        canceled = d.pop("canceled")

        job_kind = GetCompletedJobResponse200JobKind(d.pop("job_kind"))

        permissioned_as = d.pop("permissioned_as")

        is_flow_step = d.pop("is_flow_step")

        is_skipped = d.pop("is_skipped")

        workspace_id = d.pop("workspace_id", UNSET)

        parent_job = d.pop("parent_job", UNSET)

        script_path = d.pop("script_path", UNSET)

        script_hash = d.pop("script_hash", UNSET)

        args: Union[Unset, GetCompletedJobResponse200Args] = UNSET
        _args = d.pop("args", UNSET)
        if not isinstance(_args, Unset):
            args = GetCompletedJobResponse200Args.from_dict(_args)

        result: Union[Unset, GetCompletedJobResponse200Result] = UNSET
        _result = d.pop("result", UNSET)
        if not isinstance(_result, Unset):
            result = GetCompletedJobResponse200Result.from_dict(_result)

        logs = d.pop("logs", UNSET)

        deleted = d.pop("deleted", UNSET)

        raw_code = d.pop("raw_code", UNSET)

        canceled_by = d.pop("canceled_by", UNSET)

        canceled_reason = d.pop("canceled_reason", UNSET)

        schedule_path = d.pop("schedule_path", UNSET)

        flow_status: Union[Unset, GetCompletedJobResponse200FlowStatus] = UNSET
        _flow_status = d.pop("flow_status", UNSET)
        if not isinstance(_flow_status, Unset):
            flow_status = GetCompletedJobResponse200FlowStatus.from_dict(_flow_status)

        raw_flow: Union[Unset, GetCompletedJobResponse200RawFlow] = UNSET
        _raw_flow = d.pop("raw_flow", UNSET)
        if not isinstance(_raw_flow, Unset):
            raw_flow = GetCompletedJobResponse200RawFlow.from_dict(_raw_flow)

        language: Union[Unset, GetCompletedJobResponse200Language] = UNSET
        _language = d.pop("language", UNSET)
        if not isinstance(_language, Unset):
            language = GetCompletedJobResponse200Language(_language)

        get_completed_job_response_200 = cls(
            id=id,
            created_by=created_by,
            created_at=created_at,
            started_at=started_at,
            duration=duration,
            success=success,
            canceled=canceled,
            job_kind=job_kind,
            permissioned_as=permissioned_as,
            is_flow_step=is_flow_step,
            is_skipped=is_skipped,
            workspace_id=workspace_id,
            parent_job=parent_job,
            script_path=script_path,
            script_hash=script_hash,
            args=args,
            result=result,
            logs=logs,
            deleted=deleted,
            raw_code=raw_code,
            canceled_by=canceled_by,
            canceled_reason=canceled_reason,
            schedule_path=schedule_path,
            flow_status=flow_status,
            raw_flow=raw_flow,
            language=language,
        )

        get_completed_job_response_200.additional_properties = d
        return get_completed_job_response_200

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
