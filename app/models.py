from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

from config import DATABASE_URL

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session


class Question(BaseModel):
    questions_num: int


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    question = Column(String)
    created_at = Column(String)
    category_id = Column(String)
    game_id = Column(String)
