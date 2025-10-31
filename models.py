# models.py
from sqlalchemy import String, Integer, ForeignKey, Text, DateTime, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    tasks: Mapped[list["Task"]] = relationship(back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    memo: Mapped[str | None] = mapped_column(Text())
    is_done: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="0")
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    owner: Mapped[User] = relationship(back_populates="tasks")
