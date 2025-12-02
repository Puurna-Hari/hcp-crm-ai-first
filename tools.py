from langgraph.prebuilt import ToolNode
from .llm import call_llm
from ..crud import create_interaction, edit_interaction
from sqlalchemy.orm import Session
import json

# TOOL 1: Log interaction
def tool_log_interaction(db: Session, message: str):
    prompt = f"""
Extract structured fields: hcp_name, specialty, interaction_type, date, notes.
Text: {message}
Return JSON ONLY:
"""
    extracted = call_llm(prompt)
    data = json.loads(extracted)

    summary = call_llm(f"Summarize this interaction in 2 sentences: {message}")

    return create_interaction(db, data, summary)

# TOOL 2: Edit interaction
def tool_edit_interaction(db: Session, interaction_id: int, edit_message: str):
    prompt = f"""
User wants to edit interaction ID {interaction_id}.
Interpret edits and return JSON with only changed fields.
Message: {edit_message}
"""
    changes = json.loads(call_llm(prompt))
    return edit_interaction(db, interaction_id, changes)

# TOOL 3: Generate summary
def tool_generate_summary(text: str):
    return call_llm(f"Summarize: {text}")

# TOOL 4: Fetch HCP interactions
def tool_fetch(db: Session):
    from ..crud import get_interactions
    return get_interactions(db)

# TOOL 5: Suggest next best action
def tool_nba(message: str):
    return call_llm(f"Suggest pharmaceutical next-best-actions for: {message}")

# TOOL 6: Validate data
def tool_validate(raw_data: str):
    return call_llm(f"Fix missing interaction fields: {raw_data}")
