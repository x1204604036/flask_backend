
from flask.views import View, MethodView
from flask import request


class UserRegisterView(MethodView):
    methods = ["GET", "POST"]

    def get(self):
        return {"msg": "GET method OK "}

    def post(self):
        result = {"code": 0, "msg": "注册成功"}
        return result

