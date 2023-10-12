from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Quiz(Base):
    __tablename__ = 'quiz'

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True
    )
    question_id: Mapped[int] = mapped_column(Integer)
    answer: Mapped[str] = mapped_column(String)
    question: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer)
    game_id: Mapped[int] = mapped_column(Integer)
