from enum import Enum


class ListFlowsResponse200ItemValueFailureModuleValueLanguage(str, Enum):
    DENO = "deno"
    PYTHON3 = "python3"

    def __str__(self) -> str:
        return str(self.value)
