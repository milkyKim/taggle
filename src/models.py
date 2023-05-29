from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table

from src.database import Base

association_table = Table(
    "association",
    Base.metadata,
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
    Column("resource_id", Integer, ForeignKey("resource.id"), primary_key=True),
)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    resources = relationship(
        "Resource", secondary=association_table, back_populates="tags"
    )


class Resource(Base):
    __tablename__ = "resource"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    arn = Column(String, nullable=False)
    type = Column(String, nullable=False)
    region = Column(String, nullable=False)
    tags = relationship("Tag", secondary=association_table, back_populates="resources")
