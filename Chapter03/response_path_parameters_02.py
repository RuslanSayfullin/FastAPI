from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str

# Dummy database
posts = {
    1: Post(title="Hello", nb_views=100), 
}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    posts.pop(id, None)
    return None