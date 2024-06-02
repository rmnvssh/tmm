from enum import Enum

class RoutineErrors(Enum):
  WRONG_TIME = "Time is invalid"

class RoutineFrequency(Enum):
  ONCE = "ONCE"
  DAILY = "DAILY"
  WEEKLY = "WEEKLY"
  MONTHLY = "MONTHLY"

valid_routine = {
  "title": "test",
  "description": "testing",
  "timeStart": "2024-06-04T12:18:33.718",
  "timeEnd": "2024-06-04T12:18:33.718",
  "routineFrequency": "ONCE",
  "days": [
    1,
    1
  ]
}

update_valid_routine = {
  "title": "test2",
  "description": "testing2",
  "timeStart": "2024-06-05T12:18:33.718",
  "timeEnd": "2024-06-05T12:18:33.718",
  "routineFrequency": "DAILY",
  "days": [
    1,
    2
  ]
}