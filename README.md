[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


# Задание
Реализовать простой веб сервис, выполняющий следующие функции:
В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;

* После получения запроса сервис запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
* Полученные ответы должны сохраняться в базе данных, причем сохранена должна быть как минимум следующая информация: 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
* Ответом на запрос должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

# Запуск проекта

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
  "questions_count": 1
}
```

Пример ответа:
```bash
{
  "question_id": 26198,
  "question": "Some folks don't add a potent potable to Welsh rarebit but many chefs add this one",
  "answer": "beer",
  "created_at": "2022-12-30T18:48:20.401Z",
  "category_id": 63,
  "game_id": 7531
}
```

# Автор
**Михаил Кочетков** - https://github.com/MikhailKochetkov