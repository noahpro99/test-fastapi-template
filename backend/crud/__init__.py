from .crud_item import item
from .crud_user import user

from .base import CRUDBase

from models.project import Project
from schemas.project import ProjectCreate, ProjectUpdate
project = CRUDBase[Project, ProjectCreate, ProjectUpdate](Project)

from models.user_project import UserProject
from schemas.user_project import UserProjectCreate, UserProjectUpdate
user_project = CRUDBase[UserProject, UserProjectCreate, UserProjectUpdate](UserProject)

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from models.item import Item
# from schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
