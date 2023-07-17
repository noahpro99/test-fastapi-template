FROM python:3.11.4-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["sh", "-c", \
    "alembic upgrade head \
    && python initial_data.py \
    && python backend_pre_start.py \
    && uvicorn main:app --host 0.0.0.0 --port 80 \
    "]