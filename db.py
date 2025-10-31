# db.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# ✅ SQLAlchemy 2.x なら DeclarativeBase、1.4系なら declarative_base を使う
try:
    from sqlalchemy.orm import DeclarativeBase  # 2.x
    class Base(DeclarativeBase):
        pass
except ImportError:
    from sqlalchemy.orm import declarative_base  # 1.4
    Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./app.db")

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# 型ヒントはジェネレーターに合わせる／無くてもOK
from typing import AsyncIterator
async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session
