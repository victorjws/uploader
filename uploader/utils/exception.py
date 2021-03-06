from typing import Tuple

from flask import Response
from flask import jsonify


class ClientError(Exception):
    status_code = 400
    message = None
    error_num = 100

    def __init__(
        self, message: str = None, error_number: int = error_num
    ) -> None:
        self.message = message
        self.error_num = error_number

    def __repr__(self) -> str:
        return f"{ClientError.__class__.__name__}"


class ForbiddenError(ClientError):
    status_code = 403
    error_num = 101


def init_error_handler(app) -> None:
    app.register_error_handler(ClientError, client_error_handler)


def client_error_handler(error: ClientError) -> Tuple[Response, int]:
    error_info = {
        "error_name": error.__class__.__name__,
        "error_number": error.error_num,
        "message": error.message,
    }
    return jsonify(error_info), error.status_code
