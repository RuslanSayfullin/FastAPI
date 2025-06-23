from fastapi import FastAPI, Cookie

app = FastAPI

@app.get("/")
async def get_cookie(hello: str | None = Cookie(None)):
    return {"hello": hello}