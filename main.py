from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from typing import List
from fastapi import Body
from schemas import CommentUpdate
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# DB 세션 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/comments", response_model=schemas.CommentResponse)
def create(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db, comment)

@app.get("/comments", response_model=List[schemas.CommentResponse])
def get_comments(planet: str, db: Session = Depends(get_db)):
    return crud.get_comments_by_planet(db, planet)

@app.get("/comments/{comment_id}", response_model=schemas.CommentResponse)
def read(comment_id: int, db: Session = Depends(get_db)):
    comment = crud.get_comment(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Not found")
    return comment



@app.put("/comments/{comment_id}", response_model=schemas.CommentResponse)
def update(comment_id: int, payload: CommentUpdate, db: Session = Depends(get_db)):
    return crud.update_comment(db, comment_id, payload.content)

@app.delete("/comments/{comment_id}")
def delete(comment_id: int, db: Session = Depends(get_db)):
    crud.delete_comment(db, comment_id)
    return {"ok": True}
