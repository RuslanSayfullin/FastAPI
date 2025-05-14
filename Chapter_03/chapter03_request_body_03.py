from fastapi import FastAPI
from pydantic import BaseModel  # Импортируем BaseModel для создания моделей

app = FastAPI()

# Модель пользователя
class User(BaseModel):
    name: str
    age: int

# Модель компании
class Company(BaseModel):
    name: str
    location: str | None = None  # Опциональное поле
@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}