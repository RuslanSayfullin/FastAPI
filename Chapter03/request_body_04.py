from fastapi import FastAPI, Body
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def create_user(user: User, priority: int = Body(..., ge=1, le=3)):
    return {"user" : user, "priority" : priority}

# curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d '{"user": {"name": "Ruslan", "age": 30}, "priority": 1}'