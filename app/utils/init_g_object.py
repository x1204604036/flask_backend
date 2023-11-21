from flask import g, request, session


def init_g_object(app):

    @app.before_request
    def init_g_object_info():
        g.request_path = request.path
        g.user_id = session.get("user_id")
        g.ip_address = request.remote_addr
