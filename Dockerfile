FROM python:3.10-slim

WORKDIR /api

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python3", "main.py"]