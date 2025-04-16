from sqlalchemy.orm import Session
from models import Comment
from schemas import CommentCreate

def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session):
    return db.query(Comment).all()
def get_comments_by_planet(db: Session, planet: str):
    return db.query(Comment).filter(Comment.planet == planet).all()

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def update_comment(db: Session, comment_id: int, content: str):
    comment = get_comment(db, comment_id)
    if comment:
        comment.content = content
        db.commit()
    return comment

def delete_comment(db: Session, comment_id: int):
    comment = get_comment(db, comment_id)
    if comment:
        db.delete(comment)
        db.commit()
    return comment
