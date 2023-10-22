import os

if os.getenv("FLASK_ENV") == "production":
    from .production import *
else:
    from .development import *
