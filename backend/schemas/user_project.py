from datetime import date
from pydantic import BaseModel
from enums import UserProjectRole

# Shared properties
class UserProjectBase(BaseModel):
    user_id: int
    project_id: int
    start_date: date
    end_date: date|None = None
    role: UserProjectRole

# Properties to receive via API on creation
class UserProjectCreate(UserProjectBase):
    pass


# Properties to receive via API on update
class UserProjectUpdate(UserProjectBase):
    pass


class UserProjectInDBBase(UserProjectBase):
    id: int

    class Config:
        from_attributes = True


# Additional properties to return via API
class UserProject(UserProjectInDBBase):
    pass


# Additional properties stored in DB
class UserProjectInDB(UserProjectInDBBase):
    pass
