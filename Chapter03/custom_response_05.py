from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/xml")
async def get_xml():
    content = """<?xml version="1.0" encoding="UTF-8"?>
        <Hello>Hello World!</Hello>
    """
    return Response(content=content, media_type= "application/xml")

# http GET http://localhost:8000/xml