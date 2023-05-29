from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# from src.models import association_table
from src.database import Base


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    resources = relationship(
        "Resource", back_populates="tags"
    )  # secondary=association_table
