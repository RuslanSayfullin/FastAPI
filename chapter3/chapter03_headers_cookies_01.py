from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
async def get_header(hello: str = Header(...)):
    return {"hello" : hello}

# http GET http://localhost:8000 'Hello: World'