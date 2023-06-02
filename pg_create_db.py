from sqlalchemy import create_engine

from settings import DATABASE_URL
from db.models import Quiz


def main():
    engine = create_engine(DATABASE_URL)
    Quiz.metadata.create_all(engine)


if __name__ == '__main__':
    main()
