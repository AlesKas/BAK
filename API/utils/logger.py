import logging

def initLogging():
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log_fmt = "%(asctime)s:%(levelname)s: %(message)s"

    if not log.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(log_fmt)
        handler.setFormatter(formatter)
        log.addHandler(handler)

    return log