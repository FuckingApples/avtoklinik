from rest_framework.exceptions import APIException


class DetailedValidationException(APIException):
    status_code = 400
    default_detail = "Validation error"
    default_code = "validation_error"

    def __init__(self, message, code):
        self.detail = {
            "message": message,
            "code": code,
        }
