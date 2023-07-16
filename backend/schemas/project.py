from pydantic import BaseModel

from .user_project import UserProject


# Shared properties
class ProjectBase(BaseModel):
    title: str
    description: str|None = None

# Properties to receive via API on creation
class ProjectCreate(ProjectBase):
    pass


# Properties to receive via API on update
class ProjectUpdate(ProjectBase):
    pass


class ProjectInDBBase(ProjectBase):
    id: int
    user_projects: list[UserProject]

    class Config:
        from_attributes = True


# Additional properties to return via API
class Project(ProjectInDBBase):
    pass


# Additional properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
