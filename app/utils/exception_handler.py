from werkzeug.exceptions import HTTPException
from flask import jsonify


ERROR_HTTP_CODE = 417


class UserException(Exception):

    def __init__(self, code=-1, msg="error", http_code=417):
        self.code = code
        self.msg = msg
        self.http_code = http_code


def init_error_exception(app):

    @app.errorhandler(HTTPException)
    def handler_http_exception(exception):
        print(exception)
        return jsonify({"code": -1, "msg": exception.description}), exception.code

    @app.errorhandler(Exception)
    def server_exception(exception):
        print(exception)
        return jsonify({"code": -1, "msg": "内部错误"}), ERROR_HTTP_CODE

    @app.errorhandler(UserException)
    def user_exception(exception):
        print(exception)
        return jsonify({"code": exception.code, "msg": exception.msg}), exception.http_code


