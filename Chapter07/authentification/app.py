from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy import exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from password import get_password_hash
from authentication import authenticate, create_access_token
from database import get_async_session
import schemas

app = FastAPI()

@app.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRead)
async def register(
    user_create: schemas.UserCreate, 
    session: AsyncSession = Depends(get_async_session)
) -> User:
    hashed_password: get_password_hash
    user = User(*user_create.dict(exclude={"password"}), hashed_password=hashed_password)

    try:
        session.add(user)
        await session.commit()
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    
    return user

@app.post("/token")
async def create_token(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    session: AsyncSession = Depends(get_async_session),
):
    email: form_data.username
    password: form_data.password
    user = await authenticate(email, password, session)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    token = await create_access_token(user, session)

    return {"access_token": token.access_token, "token_type": "bearer"}
