from pydantic import BaseModel


class Tag(BaseModel):
    id: int
    key: str
    value: str
