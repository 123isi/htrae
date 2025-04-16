from pydantic import BaseModel
from typing import Optional

class CommentCreate(BaseModel):
    planet: str
    content: str
    author: Optional[str] = None

class CommentResponse(CommentCreate):
    id: int

    class Config:
        orm_mode = True
class CommentUpdate(BaseModel):
    content: str
