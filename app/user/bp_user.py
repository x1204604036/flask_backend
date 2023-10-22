from flask import Blueprint, request

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login", methods=("POST", "GET"))
def login():
    
    return {"code": 0, "msg": "success"}
