from enum import Enum
class TimeframeErrors(Enum):
  WRONG_TIME = "Time is invalid"

valid_timeframe = {
    "startTime": "2024-06-05T12:32:59.674",
    "endTime": "2024-06-05T13:32:59.674"
}

update_valid_timeframe = {
    "startTime": "2024-06-05T12:32:59.674",
    "endTime": "2024-06-05T14:32:59.674"
}