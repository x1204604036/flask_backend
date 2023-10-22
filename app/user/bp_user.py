from flask import Blueprint, request, session

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login", methods=("POST", "GET"))
def login():
    # username = request.form["username"]
    # password = request.form["password"]

    # 验证用户名和密码
    user_id = 1  # 进行用户名和密码验证，去数据库查询获取 user_id 信息
    if user_id:
        session.clear()
        session["user_id"] = user_id
    else:
        return {"code": -1, "msg": "用户名或密码错误"}
    return {"code": 0, "msg": "success"}


@bp.route("/logout", methods=("POST",))
def logout():
    session.clear()
    return {"code": 0, "msg": "logout success"}


def login_required(func):
    def wrapped(*args, **kwargs):
        if session.get("user_id") is None:
            return {"code": -1, "msg": "请先登录系统"}
        return func(*args, **kwargs)
    return wrapped


@bp.route("/user_info", methods=("POST",))
@login_required
def get_user_info():
    user_id = session.get("user_id")

    user_info = {"user_id": user_id}  # get user info from db
    return {"code": 0, "msg": "success", "user_info": user_info}
