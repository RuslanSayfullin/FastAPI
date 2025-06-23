from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name:str

app = FastAPI()

@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user" : user, "company" : company}

# curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d '{"user": {"name": "Alice", "age": 30}, "company": {"name": "Acme Corp"}}'