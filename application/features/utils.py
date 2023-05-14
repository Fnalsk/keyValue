from typing import Any
from flask import Response
from flask.json import jsonify as flask_jsonify


def jsonify_meta(message: Any) -> Response:
    """
    Formats a JSON response containing meta information that adheres to JSON API specification.
    """
    return flask_jsonify(**{"meta": message})


def jsonify_error(message: Any) -> Response:
    """
    Formats a JSON response containing error information that adheres to JSON API specification.
    """
    if isinstance(message, list):
        return flask_jsonify(**{"errors": message})
    return flask_jsonify(**{"errors": [message]})

