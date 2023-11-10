from werkzeug.exceptions import HTTPException
from flask import jsonify, request
import logging
import traceback


logger = logging.getLogger("error_log")


ERROR_HTTP_CODE = 417


class UserException(Exception):
    def __init__(self, code=-1, msg="error", http_code=417):
        self.code = code
        self.msg = msg
        self.http_code = http_code


def init_error_exception(app):
    @app.errorhandler(HTTPException)
    def handler_http_exception(exception):
        trace_info = traceback.format_exc()

        log_msg = "request path: %s, traceback info: %s, description: %s" % (
            request.path, trace_info, exception.description
        )
        logger.info(log_msg)
        return jsonify({"code": -1, "msg": exception.description}), exception.code

    @app.errorhandler(Exception)
    def server_exception(exception):
        logger.info("request_path: " + request.path)
        trace_info = traceback.format_exc()
        log_msg = "request path: %s, traceback info: %s" % (request.path, trace_info)
        logger.info(log_msg)
        logger.error("系统报错信息：%s" % log_msg)
        return jsonify({"code": -1, "msg": "内部错误"}), ERROR_HTTP_CODE

    @app.errorhandler(UserException)
    def user_exception(exception):
        trace_info = traceback.format_exc()
        log_msg = "request path: %s, traceback info: %s, exception msg: %s" % (
            request.path, trace_info, exception.msg
        )
        logger.info(log_msg)
        return jsonify({"code": exception.code, "msg": exception.msg}), exception.http_code


