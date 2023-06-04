from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from db.db_connection import CONNECTION_STRING


def main():
    engine = create_engine(CONNECTION_STRING)
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
