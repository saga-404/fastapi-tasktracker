# crud.py
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, Task
from schemas import TaskCreate

async def get_or_create_user(session: AsyncSession, username: str = "demo") -> User:
    res = await session.execute(select(User).where(User.username == username))
    user = res.scalar_one_or_none()
    if not user:
        user = User(username=username)
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user

async def create_task(session: AsyncSession, owner_id: int, data: TaskCreate) -> Task:
    task = Task(title=data.title, memo=data.memo, owner_id=owner_id)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

async def list_tasks(session: AsyncSession, owner_id: int) -> list[Task]:
    res = await session.execute(select(Task).where(Task.owner_id == owner_id).order_by(Task.id.desc()))
    return list(res.scalars())
