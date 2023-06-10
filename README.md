[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


# Описание
Сервис позволяет получать вопросы для викторин по запросу к публичному API https://jservice.io/api/random?count=1

## Как запустить проект:

Клонировать репозиторий:
```bash
git clone git@github.com:MikhailKochetkov/quiz_questions.git
```

Создать и активировать виртуальное окружение:
```bash
python -m venv venv
source /venv/Scripts/activate
python -m pip install --upgrade pip
```

Установить зависимости из requirements.txt:
```bash
pip install -r requirements.txt
```

Создать файл .env (шаблон наполнения размещен в файле .env.sample)

### Запуск проекта в режиме разработки:

Установить тестовый режим в настройках проекта (файл settings.py):
```bash
TEST_MODE = True
```

Запустить проект:
```bash
uvicorn main:application
```

### Запуск проекта в Docker (dockerfile):

Установить тестовый режим в настройках проекта (файл settings.py):
```bash
TEST_MODE = True
```

Собрать образ:
```bash
docker build -t api .
```

Запустить контейнер:
```bash
docker run --name quiz_questions -it -p 8000:8000 api
```

Получить ID запущенного контейнера:
```bash
docker container ls
```

Остановить контейнер:
```bash
docker container stop <CONTAINER ID>
```

### Запуск проекта в Docker (docker-compose):

Отключить тестовый режим в настройках проекта (файл settings.py):
```bash
TEST_MODE = False
```

Собрать контейнеры:
```bash
docker-compose up -d --build
```

Остановить контейнеры:
```bash
docker-compose stop
```

Остановить и удалить все контейнеры, образы, volumes:
```bash
docker-compose down -v
```

# Документация API
Документация доступна по эндпойнту:  http://127.0.0.1:8000/docs/

Пример запроса:
```bash
{
  "questions_num": 1
}
```

Пример ответа:
```bash
{
  "quiz_questions": {
    "question_id": "116337",
    "answer": "smell",
    "created_at": "2022-12-30T19:49:18.669Z",
    "game_id": "1607",
    "id": 3,
    "question": "1 reason sharks are successful predators is that large bulbs in their brains are used for this sense",
    "category_id": "717"
  }
}
```

# Автор

* **Михаил Кочетков** - https://github.com/MikhailKochetkov