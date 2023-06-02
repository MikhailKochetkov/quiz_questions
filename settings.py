import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"sqlite:///./{os.getenv('DB_NAME', default='questions.db')}"
# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/quiz_questions"
URL = os.getenv('URL', default='https://jservice.io/api/random?count=1')
HOST = os.getenv('HOST', default='127.0.0.1')
PORT = os.getenv('PORT', default=8000)
