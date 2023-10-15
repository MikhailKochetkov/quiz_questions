from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Quiz(Base):
    __tablename__ = 'quiz'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    question_id: Mapped[int] = mapped_column(Integer)
    answer: Mapped[str] = mapped_column(String)
    question: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer)
    game_id: Mapped[int] = mapped_column(Integer)
