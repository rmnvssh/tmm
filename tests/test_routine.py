import requests
import allure
import pytest

from configuration import TARPS_SERVICE_URL, PORT_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.routine import Routine
from src.enums.routine_enums import valid_routine, update_valid_routine



@allure.feature('Routine')
@allure.story('Get routine')
def test_get_routine(login_token, create_routine):
    with allure.step('Create Routine'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
    with allure.step('Get Routine'):
        r = requests.get(
            f"{TARPS_SERVICE_URL}routines/{create_routine["id"]}", headers=headers
        )
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Routine)
    with allure.step('Check Routine'):    
        assert r.json() == create_routine


@allure.feature('Routine')
@allure.story('Create routine')
def test_create_routine(login_token):
    with allure.step('Create Routine'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
        r = requests.post(
            f"{TARPS_SERVICE_URL}routines", json=valid_routine, headers=headers
        )
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Routine)
    with allure.step('Check Routine'):
        assert r.json()["title"] == valid_routine.get("title")
        assert r.json()["description"] == valid_routine.get("description")
        assert r.json()["timeStart"] == valid_routine.get(f"timeStart")
        assert r.json()["timeEnd"] == valid_routine.get("timeEnd")
        assert r.json()["routineFrequency"] == valid_routine.get("routineFrequency")
        #assert r.json()["days"] == valid_routine.get("days")


@allure.feature('Routine')
@allure.story('Get routines list')
def test_get_routines_list(login_token):
    headers = {
        "Authorization": f"Bearer {login_token}",
        "Accept": "*/*",
    }
    r = requests.get(
        f"{TARPS_SERVICE_URL}routines",
        params={"offset": 0, "limit": 10},
        headers=headers,
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Routine)


@allure.feature('Routine')
@allure.story('Update routine')
def test_update_routine(login_token, create_routine):
    with allure.step('Create Routine'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
        #new_routine = create_routine()
    with allure.step('Update Routine'):
        r = requests.put(
            f"{PORT_SERVICE_URL}routines/{create_routine["id"]}",
            json=update_valid_routine,
            headers=headers,
        )
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Routine)
    with allure.step('Check Routine'):
        assert r.json()["title"] == update_valid_routine.get("title")
        assert r.json()["description"] == update_valid_routine.get("description")
        assert r.json()["timeStart"] == update_valid_routine.get("timeStart")
        assert r.json()["timeEnd"] == update_valid_routine.get("timeEnd")
        #assert r.json()["routineFrequency"] == update_valid_routine.get("routineFrequency")
        assert r.json()["days"] == update_valid_routine.get("days")


@allure.feature('Routine')
@allure.story('Mark routine')
def test_mark_routine(login_token, create_routine):
    with allure.step('Create Routine'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
        #new_routine = create_routine()
        r = requests.put(
            f"{PORT_SERVICE_URL}routines/{create_routine["id"]}/mark-as-ended", headers=headers
        )
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Routine)
    with allure.step('Check Routine'):
        assert r.json()["id"] == create_routine["id"]
        assert r.json()["isEnded"] == True


@allure.feature('Routine')
@allure.story('Delete routine')
def test_delete_routine(login_token, create_routine):
    with allure.step('Create Routine'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
        #new_routine = create_routine()
        response = requests.delete(
            f"{PORT_SERVICE_URL}routines/{create_routine["id"]}", headers=headers
        )
        assert response.status_code == 204
    with allure.step('Is delete'):
        check = requests.get(
            f"{PORT_SERVICE_URL}routines/{create_routine["id"]}", headers=headers
        )
        assert check.status_code == 400
