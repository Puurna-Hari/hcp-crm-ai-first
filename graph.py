from langgraph.graph import StateGraph
from .state import AgentState
from .tools import (
    tool_log_interaction,
    tool_edit_interaction,
    tool_fetch,
    tool_nba,
    tool_generate_summary,
    tool_validate
)
from .llm import call_llm

def create_agent():
    graph = StateGraph(AgentState)

    def agent_node(state: AgentState):
        """Processes message and decides which tool to call"""
        msg = state["message"]

        # ROUTER LOGIC
        if "log" in msg.lower():
            state["tool"] = "log"
        elif "edit" in msg.lower():
            state["tool"] = "edit"
        elif "summary" in msg.lower():
            state["tool"] = "summary"
        elif "fetch" in msg.lower():
            state["tool"] = "fetch"
        elif "next" in msg.lower():
            state["tool"] = "nba"
        else:
            state["tool"] = "validate"

        return state

    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")

    return graph.compile()
