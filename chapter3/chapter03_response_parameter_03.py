from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str


# Dummy database
posts = {
    1: Post(title="Hello")
}

@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]
    
# http PUT http://localhost:8000/posts/2 title="Updated title"