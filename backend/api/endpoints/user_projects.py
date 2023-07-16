from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps

router = APIRouter()


@router.get("", response_model=list[schemas.UserProject])
def read_user_user_projects(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve user_user_projects.
    """
    user_user_projects = crud.user_project.get_multi(db, skip=skip, limit=limit)
    return user_user_projects

@router.post("", response_model=schemas.UserProject)
def create_user_project(
    *,
    db: Session = Depends(deps.get_db),
    user_project_in: schemas.UserProjectCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new user_project.
    """
    user_project = crud.user_project.create(db=db, obj_in=user_project_in)
    return user_project


@router.put("/{id}", response_model=schemas.UserProject)
def update_user_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    user_project_in: schemas.UserProjectUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an user_project.
    """
    user_project = crud.user_project.get(db=db, id=id)
    if not user_project:
        raise HTTPException(status_code=404, detail="UserProject not found")
    user_project = crud.user_project.update(db=db, db_obj=user_project, obj_in=user_project_in)
    return user_project


@router.get("/{id}", response_model=schemas.UserProject)
def read_user_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get user_project by ID.
    """
    user_project = crud.user_project.get(db=db, id=id)
    if not user_project:
        raise HTTPException(status_code=404, detail="UserProject not found")
    return user_project


@router.delete("/{id}", response_model=schemas.UserProject)
def delete_user_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an user_project.
    """
    user_project = crud.user_project.get(db=db, id=id)
    if not user_project:
        raise HTTPException(status_code=404, detail="UserProject not found")
    user_project = crud.user_project.remove(db=db, id=id)
    return user_project
