from datetime import datetime
from functools import wraps

from flask import request
from data.dict.dict import REQUESTS


def request_log(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        started = datetime.now()
        REQUESTS["count"] = REQUESTS["count"] + 1
        REQUESTS["last_path"] = request.path

        try:
            return view(*args, **kwargs)
        finally:
            REQUESTS["last_seconds"] = (
                datetime.now() - started
            ).total_seconds()

            print(
                "request",
                REQUESTS["count"],
                request.path,
                REQUESTS["last_seconds"],
            )

    return wrapper