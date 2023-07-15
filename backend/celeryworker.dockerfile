FROM python:3.11.4-alpine

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["sh", "-c", "python celeryworker_pre_start.py && celery -A worker worker -l info -Q main-queue -c 1"]
