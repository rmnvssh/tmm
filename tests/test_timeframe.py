import requests

from configuration import TARPS_SERVICE_URL, PORT_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.timeframe import Timeframe
from src.enums.timeframe_enums import valid_timeframe, update_valid_timeframe
from conftest import login_token, create_timeframe


def test_get_timeframe():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    new_timeframe = create_timeframe()
    r = requests.get(
        f"{TARPS_SERVICE_URL}timeframes/{new_timeframe['id']}", headers=headers
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Timeframe)
    assert r.json()["startTime"] == valid_timeframe.get("startTime")
    assert r.json()["endTime"] == valid_timeframe.get("endTime")


def test_create_timeframe():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    r = requests.post(
        f"{TARPS_SERVICE_URL}timeframes", json=valid_timeframe, headers=headers
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Timeframe)


def test_get_timeframe_list():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    r = requests.get(f"{TARPS_SERVICE_URL}timeframes", headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Timeframe)


def test_update_timeframe():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    new_timeframe = create_timeframe()
    r = requests.put(
        f"{PORT_SERVICE_URL}timeframes/{new_timeframe['id']}",
        json=update_valid_timeframe,
        headers=headers,
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Timeframe)
    assert r.json()["startTime"] == update_valid_timeframe.get("startTime")
    assert r.json()["endTime"] == update_valid_timeframe.get("endTime")


def test_delete_timeframe():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    new_timeframe = create_timeframe()
    response = requests.delete(
        f"{PORT_SERVICE_URL}timeframes/{new_timeframe['id']}", headers=headers
    )
    print(response.url)
    assert response.status_code == 200
    check = requests.get(
        f"{PORT_SERVICE_URL}timeframes/{new_timeframe['id']}", headers=headers
    )
    assert check.status_code == 400
