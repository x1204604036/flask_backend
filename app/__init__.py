from flask import Flask
from app.utils.exception_handler import init_error_exception
import logging.config
from app.config import logging_config


def create_app():
    app = Flask(__name__)
    app.secret_key = b'f0e97d3012eed1c2939ac1a62ce1e8d455e86fa9da47b26c94a9af4119be29d6'

    init_error_exception(app)
    logging.config.dictConfig(logging_config.LoggingConfig)

    @app.route("/")
    def hello():
        return "<h1>hello world</h1>"

    from . import database
    database.init_db(app)

    from .user import bp_user
    app.register_blueprint(bp_user.bp)

    return app
