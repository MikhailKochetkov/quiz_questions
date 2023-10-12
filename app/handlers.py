import json

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
        question: QuestionRequest,
        session: AsyncSession = Depends(get_session)) -> dict:
    quiz_questions = await get_quiz_questions(question.questions_count, session)
    for quiz_question in quiz_questions:
        session.add(quiz_question)
        await session.commit()
        await session.refresh(quiz_question)
    query = await session.execute(select(Quiz).order_by(Quiz.id.desc()).offset(1))
    result = query.first()
    await session.close()
    if result is None:
        return {}
    return {'quiz_questions': result}
