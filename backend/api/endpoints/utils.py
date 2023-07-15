from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic.networks import EmailStr

import models, schemas
from api import deps
from core.celery_app import celery_app
from utils_main import send_test_email

router = APIRouter()


@router.post("/test-celery/", response_model=schemas.Msg, status_code=201)
def test_celery(
    msg: schemas.Msg,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> schemas.Msg:
    """
    Test Celery worker.
    """
    celery_app.send_task("worker.test_celery", args=[msg.msg])
    return schemas.Msg(msg="Celery task sent")


@router.post("/test-email/", status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> schemas.Msg:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return schemas.Msg(msg=f"Test email sent to {email_to}")
