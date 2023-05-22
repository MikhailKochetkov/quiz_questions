import requests
from fastapi import APIRouter
from models import connect_db
from models import Quiz, Question
from config import URL

router = APIRouter()


def get_data():
    response = requests.get(URL)
    return response.json()[0]


def get_quiz_questions(num_questions):
    session = connect_db()
    quiz_questions = []
    for i in range(num_questions):
        while True:
            data = get_data()
            question = data["question"]
            answer = data["answer"]
            created_at = data["created_at"]
            category_id = data["category_id"]
            game_id = data["game_id"]
            if not session.query(Quiz).filter_by(question=question, answer=answer).first():
                break
        quiz_question = Quiz(
            question=question,
            answer=answer,
            created_at=created_at,
            category_id=category_id,
            game_id=game_id
        )
        session.add(quiz_question)
        session.commit()
        session.refresh(quiz_question)
        quiz_questions.append(quiz_question)
    session.close()
    return quiz_questions


@router.post("/quiz")
def create_quiz(question: Question):
    quiz_questions = get_quiz_questions(question.questions_num)
    return {"quiz_questions": quiz_questions}
