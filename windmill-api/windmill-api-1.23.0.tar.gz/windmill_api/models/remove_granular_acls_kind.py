from enum import Enum


class RemoveGranularAclsKind(str, Enum):
    SCRIPT = "script"
    GROUP = "group_"
    RESOURCE = "resource"
    SCHEDULE = "schedule"
    VARIABLE = "variable"
    FLOW = "flow"

    def __str__(self) -> str:
        return str(self.value)
