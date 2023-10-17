from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from db.models import Quiz
from db.session import get_session
from .schemas import QuestionRequest
from .helpers import get_quiz_questions

quiz_router = APIRouter(prefix='/api/v1')


@quiz_router.post(
    '/quiz',
    tags=['Quiz questions'],
    status_code=status.HTTP_201_CREATED)
async def create_quiz(
        request: QuestionRequest,
        session: AsyncSession = Depends(get_session)):
    quiz_questions = await get_quiz_questions(request.questions_count, session)
    for quiz_question in quiz_questions:
        session.add(quiz_question)
        await session.commit()
        await session.refresh(quiz_question)
    query = await session.execute(select(Quiz).order_by(Quiz.id.desc()).offset(1))
    result = query.first()
    await session.close()
    if result is None:
        return {}
    return {'question_id': result[0].question_id,
            'question': result[0].question,
            'answer': result[0].answer,
            'created_at': result[0].created_at,
            'category_id': result[0].category_id,
            'game_id': result[0].game_id}
