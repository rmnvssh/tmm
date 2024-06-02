from pydantic import BaseModel, validator
from datetime import datetime
from typing import List, Optional
from src.enums.task_enums import TaskErrors

class Task(BaseModel):
    id: int
    userIds: List[int]
    title: str
    description: str = None
    creationDate: Optional[datetime]
    hours: int
    period: int

@validator('creationDate')
def validate_creationDate(cls, v):
    if v is None:
        raise ValueError(TaskErrors.WRONG_TIME.value)
    else:
        return v