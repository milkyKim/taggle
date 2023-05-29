from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy import Table

from src.database import Base

from src.tag.models import Tag
from src.resource.models import Resource

association_table = Table(
    "association",
    Base.metadata,
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
    Column("resource_id", Integer, ForeignKey("resource.id"), primary_key=True),
)
