import requests

from configuration import TARPS_SERVICE_URL, PORT_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.task import Task
from src.enums.task_enums import valid_task, update_valid_task
from conftest import login_token, create_task


def test_get_task():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    new_task = create_task()
    r = requests.get(f"{TARPS_SERVICE_URL}tasks/{new_task}", headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Task)
    assert r.json()["title"] == valid_task.get("title")
    assert r.json()["description"] == valid_task.get("description")
    assert r.json()["hours"] == valid_task.get("hours")
    assert r.json()["period"] == valid_task.get("period")


def test_create_task():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    r = requests.post(f"{TARPS_SERVICE_URL}tasks", json=valid_task, headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200)


def test_get_task_list():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    r = requests.get(
        f"{TARPS_SERVICE_URL}tasks", params={"offset": 0, "limit": 10}, headers=headers
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Task)


def test_update_task():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    new_task = create_task()
    r = requests.put(
        f"{PORT_SERVICE_URL}tasks/{new_task}", json=update_valid_task, headers=headers
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Task)
    assert r.json()["title"] == update_valid_task.get("title")
    assert r.json()["description"] == update_valid_task.get("description")
    assert r.json()["hours"] == update_valid_task.get("hours")
    assert r.json()["period"] == update_valid_task.get("period")


def test_delete_task():
    headers = {
        "Authorization": f"Bearer {login_token()['accessToken']}",
        "Accept": "*/*",
    }
    new_task = create_task()
    response = requests.delete(f"{PORT_SERVICE_URL}tasks/{new_task}", headers=headers)
    print(response.url)
    assert response.status_code == 204
    check = requests.get(f"{PORT_SERVICE_URL}tasks/{new_task}", headers=headers)
    assert check.status_code == 400
