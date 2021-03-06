from flask import jsonify
from flask import request

from users import api_blueprint
from users import controller

route = api_blueprint.route


@route("/users", methods=["POST"])
def create_user():
    data = controller.create_user(
        name=request.json.get("name"), password=request.json.get("password")
    )
    return jsonify(data)


@route("/auth", methods=["POST"])
def auth():
    data = controller.auth(
        name=request.json.get("name"),
        password=request.json.get("password"),
    )
    return jsonify(data)
