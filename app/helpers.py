import requests

from sqlalchemy.sql import select

from db.models import Quiz
from settings import DESTINATION_URL


def get_data() -> dict:
    response = requests.get(DESTINATION_URL)
    return response.json()[0]


async def get_quiz_questions(num_questions, session) -> list:
    quiz_questions = []
    for num in range(num_questions):
        while True:
            data = get_data()
            result = await session.execute(select(Quiz).filter_by(question_id=data['id']))
            if not result.first():
                break
        quiz_question = Quiz(
            question_id=data['id'],
            question=data['question'],
            answer=data['answer'],
            created_at=data['created_at'],
            category_id=data['category_id'],
            game_id=data['game_id']
        )
        quiz_questions.append(quiz_question)
    return quiz_questions
