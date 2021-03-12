import os

from flask import Flask
from .app import app
from utils.logger import initLogging 

application = app.app
LOGGER = initLogging()

debug_mode = True if os.getenv("DEBUG") == 'true' else False

if __name__ == '__main__':
    if debug_mode:
        import ptvsd
        LOGGER.info("WAITING FOR DEBBUGER")
        ptvsd.enable_attach(address = ('0.0.0.0', 5678), redirect_output=True)
        ptvsd.wait_for_attach()

    LOGGER.info("Starting manager server")
    app.run(host='0.0.0.0', port=8000, debug=debug_mode, threaded=True)
