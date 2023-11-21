import logging
import time
from flask import g


logger = logging.getLogger()


class RequestLogMiddleware:

    def log_info(self):
        total_time = time.time() - g.start_time

        log_info = "request_path: {}, request_user: {}, spend_time: {}, ip_address: {}".format(
            g.request_path,
            g.user_id,
            total_time,
            g.ip_address,
        )
        logger.info(log_info)
