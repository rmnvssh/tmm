import requests
import allure

from configuration import TARPS_SERVICE_URL, PORT_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.timeframe import Timeframe
from src.enums.timeframe_enums import valid_timeframe, update_valid_timeframe



@allure.feature('Timeframe')
@allure.story('Get timeframe')
def test_get_timeframe(login_token, create_timeframe):
    with allure.step('Create Timeframe'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
        
    with allure.step('Get Timeframe'):
        r = requests.get(
            f"{TARPS_SERVICE_URL}timeframes/{create_timeframe["id"]}", headers=headers
        )
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Timeframe)
    with allure.step('Check Timeframe'):
        assert r.json()["startTime"] == valid_timeframe.get("startTime")
        assert r.json()["endTime"] == valid_timeframe.get("endTime")



@allure.feature('Timeframe')
@allure.story('Create timeframe')
def test_create_timeframe(login_token):
    headers = {
        "Authorization": f"Bearer {login_token}",
        "Accept": "*/*",
    }
    r = requests.post(
        f"{TARPS_SERVICE_URL}timeframes", json=valid_timeframe, headers=headers
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Timeframe)



@allure.feature('Timeframe')
@allure.story('Get timeframe list')
def test_get_timeframe_list(login_token):
    headers = {
        "Authorization": f"Bearer {login_token}",
        "Accept": "*/*",
    }
    r = requests.get(f"{TARPS_SERVICE_URL}timeframes", headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Timeframe)



@allure.feature('Timeframe')
@allure.story('Update timeframe')
def test_update_timeframe(login_token, create_timeframe):
    with allure.step('Create Timeframe'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }

    with allure.step('Update Timeframe'):
        r = requests.put(
            f"{PORT_SERVICE_URL}timeframes/{create_timeframe["id"]}",
            json=update_valid_timeframe,
            headers=headers,
        )
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Timeframe)
    with allure.step('Check Timeframe'):
        assert r.json()["startTime"] == update_valid_timeframe.get("startTime")
        assert r.json()["endTime"] == update_valid_timeframe.get("endTime")



@allure.feature('Timeframe')
@allure.story('Delete timeframe')
def test_delete_timeframe(login_token, create_timeframe):
    with allure.step('Create Timeframe'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
      
    with allure.step('Delete Timeframe'):
        response = requests.delete(
            f"{PORT_SERVICE_URL}timeframes/{create_timeframe["id"]}", headers=headers
        )
        print(response.url)
        assert response.status_code == 200
    with allure.step('Is deleted'):
        check = requests.get(
            f"{PORT_SERVICE_URL}timeframes/{create_timeframe["id"]}", headers=headers
        )
        assert check.status_code == 400
