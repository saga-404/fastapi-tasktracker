# schemas.py
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    memo: str | None = None

class TaskRead(BaseModel):
    id: int
    title: str
    memo: str | None
    class Config:
        from_attributes = True
