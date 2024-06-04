from enum import Enum


class UserErrors(Enum):
    WRONG_EMAIL = "Email is invalid"


valid_user = {
    "id": 52,
    "email": "shina8214@fthcapital.com",
    "password": "12345678",
    "nickname": "smirnyi",
    "firstName": "Oleg",
    "lastName": "Gorin",
}

valid_user_login = {
    "email": "shina8214@fthcapital.com",
    "password": "12345678",
    "nickname": "smirnyi",
    "firstName": "Oleg",
    "lastName": "Gorin",
}
