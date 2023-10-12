from pydantic import BaseModel


class QuestionRequest(BaseModel):
    questions_count: int


class QuestionResponse(BaseModel):
    question_id: int | None = None
    answer: str | None = None
    question: str | None = None
    created_at: str | None = None
    category_id: int | None = None
    game_id: int | None = None
