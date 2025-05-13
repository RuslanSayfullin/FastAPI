# First endpoint
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"hello" : "world"}