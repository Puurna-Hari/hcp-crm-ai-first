from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.sql import func
from .database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255))
    specialty = Column(String(255))
    interaction_type = Column(String(100))
    interaction_date = Column(Date)
    notes = Column(Text)
    summary = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
