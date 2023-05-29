from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# from src.models import association_table
from src.database import Base


class Resource(Base):
    __tablename__ = "resource"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    arn = Column(String, nullable=False)
    type = Column(String, nullable=False)
    region = Column(String, nullable=False)
    tags = relationship(
        "Tag", back_populates="resources"
    )  # secondary=association_table
