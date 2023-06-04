FROM python:3.10-slim

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . /api

CMD ["uvicorn", "main:application", "--host", "0.0.0.0", "--port", "8000"]