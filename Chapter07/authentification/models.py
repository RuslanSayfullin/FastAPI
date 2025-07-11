from datetime import datetime, timezone, timedelta

from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship 


def get_expiration_date(duration_seconds: int=86400) -> datetime:
    return datetime.now(tz=timezone.utc) + timedelta(seconds=duration_seconds)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(1024), index=True, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=True)


class AccessToken(Base):
    __tablename__ = "access_tokens"

    access_token: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=get_expiration_date)
    user: Mapped[User] = relationship("User", lazy="joined")

