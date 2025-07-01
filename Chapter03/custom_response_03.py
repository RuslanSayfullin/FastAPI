from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/redirect")
async def redirect():
    return RedirectResponse("new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)

# http GET http://localhost:8000/redirect