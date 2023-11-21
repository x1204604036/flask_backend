# app/utils/middlewares/middlewares.py

from .login_required_middleware import LoginRequiredMiddleware
from .request_log_middleware import RequestLogMiddleware
from flask import g
import time


def register_middleware(app):

    @app.before_request
    def record_start_time():
        g.start_time = time.time()

    @app.before_request
    def login_required():
        LoginRequiredMiddleware().check()

    @app.after_request
    def request_log_info(response):
        RequestLogMiddleware().log_info()
        return response

    # @app.before_request
    # def before_request_test():
    #     print("before request")
    #
    # @app.after_request
    # def after_request_test(response):
    #     print("after request")
    #     return response
