from pydantic import BaseModel
from datetime import date

class InteractionBase(BaseModel):
    hcp_name: str | None = None
    specialty: str | None = None
    interaction_type: str | None = None
    interaction_date: date | None = None
    notes: str | None = None

class InteractionCreate(InteractionBase):
    pass

class InteractionEdit(BaseModel):
    id: int
    changes: dict

class InteractionResponse(InteractionBase):
    id: int
    summary: str | None

    class Config:
        orm_mode = True
