from fastapi import FastAPI, Header, HTTPException, status, Depends

app = FastAPI()

def secret_header(secret_header: str | None = Header(None)) -> None:
    if not secret_header or secret_header != "SWCRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)
    
@app.get("/protected-route", dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}

