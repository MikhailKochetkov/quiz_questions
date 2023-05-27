from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    answer = Column(String)
    question = Column(String)
    created_at = Column(String)
    category_id = Column(String)
    game_id = Column(String)
