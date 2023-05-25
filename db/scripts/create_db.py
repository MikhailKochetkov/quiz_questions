from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from settings import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())
    session.execute(text("""create table quiz (
    id integer not null primary key,
    question_id varchar(256),
    answer varchar(256),
    question varchar(256),
    created_at varchar(256),
    category_id varchar(256),
    game_id varchar(256)
    );"""))
    session.close()


if __name__ == '__main__':
    main()
