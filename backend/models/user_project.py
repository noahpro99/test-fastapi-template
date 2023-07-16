from datetime import date
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enums import UserProjectRole

from db.base_class import Base

class UserProject(Base):
    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="user_projects", foreign_keys=[user_id])
    
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    project = relationship("Project", back_populates="user_projects", foreign_keys=[project_id])
    
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    role = Column(Enum(UserProjectRole), nullable=False)