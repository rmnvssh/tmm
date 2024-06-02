import re
from urllib import response
import requests

from configuration import USER_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import Authentication, User
from src.enums.user_enums import valid_user, valid_user_login
from conftest import login_token
    
    
def test_login():
    r = requests.post(f'{USER_SERVICE_URL}auth/log-in', json = valid_user_login)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Authentication)


def test_refresh_token():
    refreshToken = login_token()['refreshToken']
    r = requests.get(f'{USER_SERVICE_URL}auth/refresh',
                            params={'refreshToken': refreshToken, 'userId': valid_user.get('id')})
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Authentication)


def test_get_user():
    headers = {'Authorization': f'Bearer {login_token()['accessToken']}', 'Accept': '*/*'}
    r = requests.get(f'{USER_SERVICE_URL}users/{valid_user.get('id')}', headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(User)
    assert r.json()['id'] == valid_user.get('id')
    assert r.json()['email'] == valid_user.get('email')



    

    
    