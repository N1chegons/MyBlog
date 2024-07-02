from pydantic import BaseModel
from datetime import datetime
class Post(BaseModel):
    id: int
    title: str
    description: str
    data: datetime

    class Config:
        from_attributes = True


