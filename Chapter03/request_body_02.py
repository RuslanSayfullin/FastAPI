from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def create_user(user: User):
    return user

# http -v POST http://localhost:8000/users name="John" age=30