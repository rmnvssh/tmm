import requests
import allure

from configuration import TARPS_SERVICE_URL, PORT_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.task import Task
from src.enums.task_enums import valid_task, update_valid_task



@allure.feature('Task')
@allure.story('Get task')
def test_get_task(login_token, task_id):
    with allure.step('Create Task'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
        
        r = requests.get(f"{TARPS_SERVICE_URL}tasks/{task_id}", headers=headers)
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Task)
    with allure.step('Check Task'):
        assert r.json()["title"] == valid_task.get("title")
        assert r.json()["description"] == valid_task.get("description")
        assert r.json()["hours"] == valid_task.get("hours")
        assert r.json()["period"] == valid_task.get("period")



@allure.feature('Task')
@allure.story('Create task')
def test_create_task(login_token):
    headers = {
        "Authorization": f"Bearer {login_token}",
        "Accept": "*/*",
    }
    r = requests.post(f"{TARPS_SERVICE_URL}tasks", json=valid_task, headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200)



@allure.feature('Task')
@allure.story('Get tasks list')
def test_get_task_list(login_token):
    headers = {
        "Authorization": f"Bearer {login_token}",
        "Accept": "*/*",
    }
    r = requests.get(
        f"{TARPS_SERVICE_URL}tasks", params={"offset": 0, "limit": 10}, headers=headers
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Task)



@allure.feature('Task')
@allure.story('Update task')
def test_update_task(login_token, task_id):
    with allure.step('Create Task'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
    with allure.step('Update Task'):
        r = requests.put(
            f"{PORT_SERVICE_URL}tasks/{task_id}", json=update_valid_task, headers=headers
        )
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(Task)
    with allure.step('Check Task'):
        assert r.json()["title"] == update_valid_task.get("title")
        assert r.json()["description"] == update_valid_task.get("description")
        assert r.json()["hours"] == update_valid_task.get("hours")
        assert r.json()["period"] == update_valid_task.get("period")



@allure.feature('Task')
@allure.story('Delete task')
def test_delete_task(login_token, task_id):
    with allure.step('Create Task'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
    with allure.step('Delete Task'):
        response = requests.delete(f"{PORT_SERVICE_URL}tasks/{task_id}", headers=headers)
        print(response.url)
        assert response.status_code == 204
    with allure.step('Is delete'):
        check = requests.get(f"{PORT_SERVICE_URL}tasks/{task_id}", headers=headers)
        assert check.status_code == 400
