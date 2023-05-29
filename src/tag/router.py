from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Tag

router = APIRouter(
    prefix="/api/tag",
)


@router.get("/list")
def tag_list(db: Session = Depends(get_db)):
    _tag_list = db.query(Tag).order_by(Tag.create_date.desc()).all()
    return _tag_list
