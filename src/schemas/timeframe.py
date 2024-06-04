from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional
from src.enums.timeframe_enums import TimeframeErrors


class Timeframe(BaseModel):
    id: int
    userId: int
    startTime: Optional[datetime]
    endTime: Optional[datetime]

    @field_validator("startTime")
    def validate_starttime(cls, v):
        if v is None:
            raise ValueError(TimeframeErrors.WRONG_TIME.value)
        else:
            return v
