from typing import TypedDict

class AgentState(TypedDict):
    message: str
    tool: str | None
    result: str | None
