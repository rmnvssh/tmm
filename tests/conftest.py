import pytest
import requests

from configuration import USER_SERVICE_URL, TARPS_SERVICE_URL
from src.enums.user_enums import valid_user_login
from src.enums.routine_enums import valid_routine
from src.enums.task_enums import valid_task
from src.enums.timeframe_enums import valid_timeframe


def login_token():
    response = requests.post(f"{USER_SERVICE_URL}auth/log-in", json=valid_user_login)
    return response.json()


def create_routine():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    response = requests.post(
        f"{TARPS_SERVICE_URL}routines", json=valid_routine, headers=headers
    )
    return response.json()


def create_task():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
        "Content-Type": "application/json",
    }
    taskId = requests.post(
        f"{TARPS_SERVICE_URL}tasks", json=valid_task, headers=headers
    )
    return taskId.json()


def create_timeframe():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
        "Content-Type": "application/json",
    }
    response = requests.post(
        f"{TARPS_SERVICE_URL}timeframes", json=valid_timeframe, headers=headers
    )
    return response.json()
