from src.enums.global_enums import GlobalErrorMessages
from pydantic import BaseModel


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert (
                self.response_status in status_code
            ), GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert (
                self.response_status == status_code
            ), GlobalErrorMessages.WRONG_STATUS_CODE.value

        return self

    def __str__(self):
        return (
            f"\nStatus code: {self.response_status} \n"
            f"Requested url: {self.response.url} \n"
            f"Response body: {self.response_json}"
        )
