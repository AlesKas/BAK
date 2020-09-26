import os
import connexion

from flask import Flask
from utils.logging import LOGGER
#from utils.db import db_util
from connexion.resolver import RestyResolver
from swagger_ui_bundle import swagger_ui_3_path

def create_app():
    app = connexion.App("Network attached storage", options={'swagger_ui': True, 'swagger_path': swagger_ui_3_path}, specification_dir='')
    app.app.url_map.strict_slashes = False
    app.add_api('manager.specs.yaml',
                resolver=RestyResolver('api'),
                validate_responses=True,
                strict_validation=True)

    @app.app.after_request
    def _set_headers(response):
        LOGGER.info("MSG")
        return response

    @app.app.before_request
    def _db_connect():
        try:
            pass
        except:
            pass
        print("ERRRR")
        LOGGER.info("Setting un db")

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)