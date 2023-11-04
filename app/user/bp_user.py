from flask import Blueprint, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.database import db_session


bp = Blueprint("user", __name__, url_prefix="/user")


def register():
    request_json = request.json
    username = request_json.get("username")
    password = request_json.get("password")
    email = request_json.get("email")

    if not username or not password or not email:
        return {"code": -1, "msg": "请传递用户名、密码、邮件等必要信息"}

    user = User.query.filter(User.username == username, User.email == email).first()

    if user:
        return {"code": -1, "msg": "用户已存在"}

    new_user = User(
        username=username,
        email=email,
        password=generate_password_hash(password)
    )
    db_session.add(new_user)
    db_session.commit()

    return {"code": 0, "msg": "注册成功"}


@bp.route("/login", methods=("POST", "GET"))
def login():
    username = request.form["username"]
    password = request.form["password"]

    if not username or not password:
        return {"code": -1, "msg": "请上传用户名和密码"}

    user = User.query.filter(User.username == username).first()
    if not user:
        return {"code": -1, "msg": "用户不存在"}

    if not check_password_hash(user.password, password):
        return {"code": -1, "msg": "密码验证失败"}

    session.clear()
    session["user_id"] = user.id

    return {"code": 0, "msg": "success"}


def login_required(func):
    def wrapped(*args, **kwargs):
        if session.get("user_id") is None:
            return jsonify({"code": -1, "msg": "请先登录系统"}), 401
        return func(*args, **kwargs)
    return wrapped


@bp.route("/logout", methods=("POST",))
def logout():
    session.clear()
    return {"code": 0, "msg": "logout success"}


@bp.route("/user_info", methods=("POST",))
@login_required
def get_user_info():
    user_id = session.get("user_id")

    user_info = {"user_id": user_id}  # get user info from db
    return {"code": 0, "msg": "success", "user_info": user_info}
