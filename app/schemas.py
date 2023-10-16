from pydantic import BaseModel


class QuestionRequest(BaseModel):
    questions_count: int
