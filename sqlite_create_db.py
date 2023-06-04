from sqlalchemy import create_engine

from db.db_connection import CONNECTION_STRING
from db.models import Quiz


def main():
    engine = create_engine(CONNECTION_STRING)
    Quiz.metadata.create_all(engine)


if __name__ == "__main__":
    main()
