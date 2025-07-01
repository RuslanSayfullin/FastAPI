from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def custom_headers(response: Response):
    response.headers["Custom-Headers"] = "Custom-Header-Value"
    return {"hello": "world"}

# http GET http://localhost:8000