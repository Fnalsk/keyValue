from typing import Tuple

from flask import Response

from application.exceptions import NotFound
from application.extensions import db, db_lock
from application.features.utils import jsonify_meta


def store_value(key: str, value: str) -> Tuple[Response, bool]:
    """
    Stores the given key value pair in the database.

    If the key already exists, overwrite the existing value.
    """
    overwritten = False
    if key in db:
        overwritten = True
    db_lock.acquire()
    db[key] = value
    db_lock.release()
    return jsonify_meta(f"Successfully stored key: {key}, value: {value}"), overwritten


def get_value(key: str) -> Response:
    """
    Attempt to retrieve the value at the given key.
    """
    if key in db:
        return jsonify_meta({
            "value": db[key]
        })
    raise NotFound(f"Key {key} does not exist in db.")


def delete_key(key: str) -> Response:
    """
    Attempt to delete a key from the database.
    """
    if key in db:
        db_lock.acquire()
        del db[key]
        db_lock.release()
        return jsonify_meta(f"Successfully deleted key: {key}")
    return jsonify_meta(f"Key {key} does not exist in db.")






