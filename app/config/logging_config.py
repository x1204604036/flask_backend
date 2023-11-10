# app/config/logging_config.py

from app.config import config

LoggingConfig = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(filename)s %(lineno)s %(message)s",
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "filename": config.LOGGING_PATH,
            "formatter": "verbose",
            "class": "logging.handlers.RotatingFileHandler",
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 20,
        },
        "error_handler": {
            "level": "INFO",
            "filename": config.LOGGING_ERROR_PATH,
            "formatter": "verbose",
            "class": "logging.handlers.RotatingFileHandler",
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 20,
        },
        "email_handler": {
            "level": "WARNING",
            "class": "logging.handlers.SMTPHandler",
            "mailhost": ("smtp.163.com", 25),
            "fromaddr": "hunterxxxxx@163.com",
            "toaddrs": "120xxxxx@qq.com",
            "subject": "系统error",
            "credentials": ("hunterxxxxx@163.com", "JBDMVIXxxxxxx"),
            "timeout": 20,
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "INFO",
        "propagate": True,
    },
    "loggers": {
        "error_log": {
            "handlers": ["error_handler", "email_handler"],
            "level": "INFO",
        }
    }
}