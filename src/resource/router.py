from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Resource

router = APIRouter(
    prefix="/api/resource",
)
