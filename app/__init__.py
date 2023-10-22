from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    def hello():
        return "<h1>hello world</h1>"

    from .user import bp_user
    app.register_blueprint(bp_user.bp)

    return app
