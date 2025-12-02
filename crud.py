from sqlalchemy.orm import Session
from . import models, schemas

def create_interaction(db: Session, data: schemas.InteractionCreate, summary: str):
    db_item = models.Interaction(
        hcp_name=data.hcp_name,
        specialty=data.specialty,
        interaction_type=data.interaction_type,
        interaction_date=data.interaction_date,
        notes=data.notes,
        summary=summary
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def edit_interaction(db: Session, interaction_id: int, changes: dict):
    db_item = db.query(models.Interaction).filter(models.Interaction.id == interaction_id).first()
    if not db_item:
        return None

    for key, value in changes.items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

def get_interactions(db: Session):
    return db.query(models.Interaction).all()
