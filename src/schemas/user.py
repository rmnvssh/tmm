from pydantic import BaseModel, validator
from datetime import datetime
from typing import List, Optional
from src.enums.user_enums import UserErrors
import re

class User(BaseModel):
    id: int
    email: str
    nickname: str = None
    firstName: str = None
    lastName: str = None
    creationDate: Optional[datetime]
    
    
    @validator('email')
    def validate_email(cls, value):
        if not bool(re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', value)):
            raise ValueError(UserErrors.WRONG_EMAIL.value)
        return value
    
class Authentication(BaseModel):
    type: str
    accessToken: str
    refreshToken: str
    
    @validator('type')
    def check_type(cls, value):
        if value != "Bearer":
            raise ValueError("Wrong type")
        return value