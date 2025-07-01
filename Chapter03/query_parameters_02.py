from enum import Enum
from fastapi import FastAPI

class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

app = FastAPI()

@app.get("/users")
async def get_user(format: UsersFormat):
    return {"format": format}

# 'http://localhost:8000/users?format=short'