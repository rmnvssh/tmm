import requests

from configuration import TARPS_SERVICE_URL, PORT_SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.routine import Routine
from src.enums.routine_enums import valid_routine, update_valid_routine
from conftest import login_token, create_routine

def test_get_routine():
    headers = {'Authorization': f'Bearer {login_token()['accessToken']}', 'Accept': '*/*'}
    new_routine = create_routine()
    r = requests.get(f'{TARPS_SERVICE_URL}routines/{new_routine['id']}', headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Routine)
    assert r.json() == new_routine

def test_create_routine():
    headers = {'Authorization': f'Bearer {login_token()['accessToken']}', 'Accept': '*/*'}
    r = requests.post(f'{TARPS_SERVICE_URL}routines', json=valid_routine, headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Routine)
    assert r.json()['title'] == valid_routine.get('title')
    assert r.json()['description'] == valid_routine.get('description')
    assert r.json()['timeStart'] == valid_routine.get(f'timeStart')
    assert r.json()['timeEnd'] == valid_routine.get('timeEnd')
    assert r.json()['routineFrequency'] == valid_routine.get('routineFrequency')


def test_get_routines_list():
    headers = {'Authorization': f'Bearer {login_token()['accessToken']}', 'Accept': '*/*'}
    r = requests.get(f'{TARPS_SERVICE_URL}routines', params={'offset': 0, 'limit': 10}, headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Routine)

def test_update_routine():
    headers = {'Authorization': f'Bearer {login_token()['accessToken']}', 'Accept': '*/*'}
    new_routine = create_routine()
    r = requests.put(f'{PORT_SERVICE_URL}routines/{new_routine['id']}', json=update_valid_routine, headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Routine)
    assert r.json()['title'] == update_valid_routine.get('title')
    assert r.json()['description'] == update_valid_routine.get('description')
    assert r.json()['timeStart'] == update_valid_routine.get('timeStart')
    assert r.json()['timeEnd'] == update_valid_routine.get('timeEnd')
    assert r.json()['days'] == update_valid_routine.get('days')

def test_mark_routine():
    headers = {'Authorization': f'Bearer {login_token()['accessToken']}', 'Accept': '*/*'}
    new_routine = create_routine()
    r = requests.put(f'{PORT_SERVICE_URL}routines/{new_routine['id']}/mark-as-ended', headers=headers)
    response = Response(r)
    print(response)
    response.assert_status_code(200).validate(Routine)
    assert r.json()['id'] == new_routine['id']
    assert r.json()['isEnded'] == True

def test_delete_routine():
    headers = {'Authorization': f'Bearer {login_token()['accessToken']}', 'Accept': '*/*'}
    new_routine = create_routine()
    response = requests.delete(f'{PORT_SERVICE_URL}routines/{new_routine['id']}', headers=headers)
    assert response.status_code == 204
    check = requests.get(f'{PORT_SERVICE_URL}routines/{new_routine['id']}', headers=headers)
    assert check.status_code == 400

