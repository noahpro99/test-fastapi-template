from celery import Celery
from celery.schedules import crontab
celery_app = Celery("worker", broker="amqp://guest@queue//")
celery_app.conf.task_routes = {"worker.test_celery": "main-queue"}


import worker  # noqa


@celery_app.on_after_configure.connect  # type: ignore
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="*/1"),
        worker.test_celery.s("hello"),
        name="test every minute",
    )
