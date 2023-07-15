from celery import Celery
from celery.schedules import crontab

celery_app = Celery("worker", broker="amqp://guest@queue//")

celery_app.conf.task_routes = {"worker.test_celery": "main-queue"}

@celery_app.on_after_configure.connect  # type: ignore
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        # every minute
        crontab(),
        sender.send_task("worker.test_celery", args=["hello"]),
    )
