import re
from urllib import response
import requests
import allure

from configuration import USER_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import Authentication, User
from src.enums.user_enums import valid_user, valid_user_login


@allure.feature('User')
@allure.story('Login')
def test_login():
    r = requests.post(f"{USER_SERVICE_URL}auth/log-in", json=valid_user_login)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Authentication)



@allure.feature('User')
@allure.story('Refresh')
def test_refresh_token(refresh_token):
    r = requests.get(
        f"{USER_SERVICE_URL}auth/refresh",
        params={"refreshToken": refresh_token, "userId": valid_user.get("id")},
    )
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Authentication)



@allure.feature('User')
@allure.story('Get user')
def test_get_user(login_token):
    with allure.step('Get user'):
        headers = {
            "Authorization": f"Bearer {login_token}",
            "Accept": "*/*",
        }
        r = requests.get(f"{USER_SERVICE_URL}users/{valid_user.get('id')}", headers=headers)
        response = Response(r)
        print(response)
        response.assert_status_code(200).validate(User)
    with allure.step('Check user'):
        assert r.json()["id"] == valid_user.get("id")
        assert r.json()["email"] == valid_user.get("email")
