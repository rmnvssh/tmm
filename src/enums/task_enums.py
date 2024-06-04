from enum import Enum


class TaskErrors(Enum):
    WRONG_TIME = "Time is invalid"


valid_task = {"title": "test", "description": "testing", "hours": 4, "period": 1}

update_valid_task = {
    "title": "test_test",
    "description": "testing",
    "hours": 2,
    "period": 2,
}
