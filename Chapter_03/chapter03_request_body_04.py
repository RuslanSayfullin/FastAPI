from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# Модель пользователя
class User(BaseModel):
    name: str
    age: int

@app.post("/users")
async def create_user(user: User, priority: int = Body(..., ge=1,
le=3)):
    return {"user": user, "priority": priority}