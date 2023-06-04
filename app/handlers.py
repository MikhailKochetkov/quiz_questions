import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.models import Quiz
from db.session import get_db
from .schemas import Question
from settings import DESTINATION_URL

router = APIRouter()


def get_data() -> dict:
    response = requests.get(DESTINATION_URL)
    return response.json()[0]


def get_quiz_questions(num_questions) -> list:
    session = next(get_db())
    quiz_questions = []
    for num in range(num_questions):
        while True:
            data = get_data()
            if not session.query(Quiz).filter_by(question_id=data["id"]).first():
                break
        quiz_question = Quiz(
            question_id=data["id"],
            question=data["question"],
            answer=data["answer"],
            created_at=data["created_at"],
            category_id=data["category_id"],
            game_id=data["game_id"]
        )
        quiz_questions.append(quiz_question)
    return quiz_questions


@router.post("/quiz", tags=["Save questions"])
async def create_quiz(
        question: Question,
        session: Session = Depends(get_db)) -> dict:
    quiz_questions = get_quiz_questions(question.questions_num)
    for quiz_question in quiz_questions:
        session.add(quiz_question)
        session.commit()
        session.refresh(quiz_question)
    session.close()
    return {"quiz_questions": session.query(Quiz).order_by(Quiz.id.desc()).offset(1).first()}
