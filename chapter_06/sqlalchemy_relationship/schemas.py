from datetime import datetime
from pydantic import BaseModel, Field

class CommentBase(BaseModel):
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str

    class Config:
        orm_mode = True

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int
    post_id: int

class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)
   
class PostRead(PostBase):
    id: int
    comments: list[CommentRead]