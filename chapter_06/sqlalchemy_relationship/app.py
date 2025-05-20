import contextlib
from fastapi import FastAPI, Depends, status, Query, HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from chapter_06.sqlalchemy_relationship import schemas
from chapter_06.sqlalchemy_relationship.database import (
    create_all_tables,
    get_async_session,
)
from chapter_06.sqlalchemy_relationship.models import Comment, Post

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)


async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_post_or_404(
    id: int, session: AsyncSession = Depends(get_async_session)
) -> Post:
    select_query = (
        select(Post).options(selectinload(Post.comments)).where(Post.id == id)
    )
    result = await session.execute(select_query)
    post = result.scalar_one_or_none()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return post

@app.post("/posts/{id}/comments", 
          response_model=schemas.CommentRead, 
          status_code=status.HTTP_201_CREATED,)
async def create_comment(
    comment_create: schemas.CommentCreate,
    post: Post = Depends(get_post_or_404),
    session: AsyncSession = Depends(get_async_session),
) -> Comment:
    comment = Comment(**comment_create.dict(), post=post)
    session.add(comment)
    await session.commit()

    return comment