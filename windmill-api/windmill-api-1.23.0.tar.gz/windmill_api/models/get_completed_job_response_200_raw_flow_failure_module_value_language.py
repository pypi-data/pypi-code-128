from enum import Enum


class GetCompletedJobResponse200RawFlowFailureModuleValueLanguage(str, Enum):
    DENO = "deno"
    PYTHON3 = "python3"

    def __str__(self) -> str:
        return str(self.value)
