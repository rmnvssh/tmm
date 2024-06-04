from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List, Optional
from src.enums.routine_enums import RoutineFrequency, RoutineErrors


class Routine(BaseModel):
    id: int
    userIds: List[int]
    title: str
    description: str
    timeStart: Optional[datetime]
    timeEnd: Optional[datetime]
    routineFrequency: RoutineFrequency
    days: List[int] | None
    isEnded: bool

    @field_validator("timeStart")
    def validate_timeStart(cls, v):
        if v is None:
            raise ValueError(RoutineErrors.WRONG_TIME.value)
        else:
            return v

    @field_validator("timeEnd")
    def validate_timeEnd(cls, v):
        if v is None:
            raise ValueError(RoutineErrors.WRONG_TIME.value)
        else:
            return v
