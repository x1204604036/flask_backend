from flask import g
from app.utils.exception_handler import UserException


class LoginRequiredMiddleware:

    def check_login(self):
        return True if g.user_id is not None else False

    def check_login_essential(self):
        url_path = g.request_path
        outer_url_list = ["/user/login", "/user/register"]
        return True if url_path not in outer_url_list else False

    def check(self):
        need_check = self.check_login_essential()

        if need_check:
            if not self.check_login():
                raise UserException(code=-1, msg="not login", http_code=401)

