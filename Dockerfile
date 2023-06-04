FROM python:3.10-slim

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . /api

ENV URL="https://jservice.io/api/random?count=1"

CMD ["uvicorn", "main:application", "--host", "0.0.0.0", "--port", "8000"]