# main.py
import os
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv

from db import Base, engine, get_session
from crud import get_or_create_user, create_task, list_tasks
from schemas import TaskCreate, TaskRead

load_dotenv()
app = FastAPI(title=os.getenv("APP_NAME", "Task & Time Tracker"))
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # 開発初期はオートマイグレーションでOK（後でAlembicに切替）
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"ok": True}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tasks", response_model=list[TaskRead])
async def get_tasks(session: AsyncSession = Depends(get_session)):
    user = await get_or_create_user(session)
    tasks = await list_tasks(session, user.id)
    return tasks

@app.post("/tasks", response_model=TaskRead)
async def post_task(data: TaskCreate, session: AsyncSession = Depends(get_session)):
    user = await get_or_create_user(session)
    task = await create_task(session, user.id, data)
    return task
