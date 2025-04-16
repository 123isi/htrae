from sqlalchemy import Column, Integer, String
from database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    author = Column(String, nullable=False)
    planet = Column(String, nullable=False)