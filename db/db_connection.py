import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = (f'{os.getenv("DATABASE_URL", default="sqlite:///")}'
                     f'./{os.getenv("DB_NAME", default="questions.db")}')

PG_CONNECTION_STRING = (f'{os.getenv("PG_DATABASE_URL", default="postgresql://")}'
                        f'{os.getenv("DB_USER", default="postgres")}:'
                        f'{os.getenv("DB_PASSWORD", default="postgres")}@'
                        f'{os.getenv("DB_HOST", default="127.0.0.1")}:'
                        f'{os.getenv("DB_PORT", default=5432)}/'
                        f'{os.getenv("PG_DB_NAME", default="questions")}')