from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
async def root(id: int):
    return {"id" : id}