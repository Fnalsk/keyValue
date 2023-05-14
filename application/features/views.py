from flask import request

from application.exceptions import BaseFlaskException
from application.features import core
from application.features.utils import jsonify_error


def register_base_routes(app):
    @app.route("/", methods=["GET", "POST", "PATCH"])
    def hello():
        return "Hello world", 200

    @app.route("/store-value", methods=["POST", "PATCH"])
    def store_value():
        data = request.get_json(force=True).get("meta")
        response, overwritten = core.store_value(
            data['key'],
            data['value']
        )
        return response, 200 if overwritten else 201

    @app.route("/get-value/<string:key>", methods=["GET"])
    def get_value(key: str):
        try:
            return core.get_value(
                key
            ), 200
        except BaseFlaskException as e:
            return jsonify_error(e.message), e.status

    @app.route("/delete-key/<string:key>", methods=["DELETE"])
    def delete_key(key: str):
        return core.delete_key(
            key
        ), 200




