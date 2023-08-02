# test-fastapi-template

## Setup Instructions

[Install Docker](https://docs.docker.com/get-docker/)

Create a copy of the `.env.example` file and name it `.env`. Update the values in the `.env` file to match your environment. 

## Development
```
docker compose -f docker-compose.dev.yml up --build --remove-orphans
```

## To manually run a task

```
docker exec <stack_name-celeryworker-1> python manage/run_celery_task.py <task_name> <task_args>
```


## Stack
- Docker (Containerization)
- FastAPI (Web Framework)
- Celery (Task Queue)
- Alembic (DB Migrations)
- Traefik (Reverse Proxy)