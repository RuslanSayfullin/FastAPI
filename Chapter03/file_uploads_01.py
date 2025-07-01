from fastapi import FastAPI, File

app = FastAPI()

@app.post("/files")
async def upload_file(file: bytes = File(...)):
    # return size of the file in bytes
    return{"file size" : len(file)}
