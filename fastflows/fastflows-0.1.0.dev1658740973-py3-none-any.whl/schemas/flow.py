import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from fastflows.schemas.deployment import DeploymentInputParams
from fastflows.schemas.flow_data import FlowData
from fastflows.config.app import configuration as cfg


# before prefect call
class FlowDeployInput(BaseModel):
    """REST Create flow Input model"""

    flows_home_path: Optional[str] = cfg.FLOWS_HOME
    flow_data: Optional[FlowData]
    flow_name: Optional[str]
    flow_path: Optional[str]
    deployment_params: Optional[DeploymentInputParams]
    force: bool = Field(False, description="Force deploy all flows")


# Flow Data after communication with Prefect
class Flow(BaseModel):
    """Created in Prefect Flow with deployment"""

    id: str
    name: str
    file_path: Optional[str]
    deployment_id: str
    deployment_name: str
    version: int


class PrefectFlowResponse(BaseModel):

    name: str
    tags: List[str] = Field(default_factory=list)
    id: str
    created: datetime.datetime
    updated: datetime.datetime
