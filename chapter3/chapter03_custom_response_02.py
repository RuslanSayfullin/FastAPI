from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/redirect")
async def redirect():
    return RedirectResponse("new-url")

# http GET http://localhost:8000/redirect