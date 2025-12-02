from fastapi import FastAPI
from .database import Base, engine
from .routes import interactions, chat

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(interactions.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

@app.get("/")
def home():
    return {"msg": "AI CRM Backend Running"}
