from fastapi import FastAPI, Header, Depends

app = FastAPI()

async def pagination(skip: int = 0, limit: int = 10) -> tuple[int, int]:
    return (skip, limit)

@app.get("/items")
async def list_items(p: tuple[int, int] = Depends(pagination)):
    # http "http://localhost:8000/items?limit=5&skip=10"
    skip, limit = p
    return {"skip": skip, "limit": limit}

@app.get("/things")
async def list_things(p: tuple[int, int] = Depends(pagination)):
    # http "http://localhost:8000/things?limit=5&skip=10"
    skip, limit = p
    return {"skip": skip, "limit": limit}

