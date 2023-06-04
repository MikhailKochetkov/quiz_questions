from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db_connection import CONNECTION_STRING, PG_CONNECTION_STRING
from settings import TEST_MODE
from .models import Quiz, Base


if TEST_MODE:
    engine = create_engine(CONNECTION_STRING, connect_args={"check_same_thread": False})
    Quiz.metadata.create_all(engine)
    SessionLocal = sessionmaker(autoflush=False, bind=engine)
else:
    engine = create_engine(PG_CONNECTION_STRING)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
