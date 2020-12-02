import connexion

from flask import Flask, abort
from utils.db import db_util
from peewee import OperationalError
from utils.logger import initLogging
from connexion.resolver import RestyResolver
from swagger_ui_bundle import swagger_ui_3_path

LOGGER = initLogging()

def create_app():
    LOGGER.info("creating manager API")
    app = connexion.App("Network attached storage", options={'swagger_ui': True, 'swagger_path': swagger_ui_3_path}, specification_dir='')
    app.app.url_map.strict_slashes = False
    app.add_api('/storage/manager.specs.yaml',
                resolver=RestyResolver('api'),
                validate_responses=True,
                strict_validation=True)

    @app.app.after_request
    def _set_headers(response):
        return response

    @app.app.before_request
    def _db_connect():
        try:
            db_util.DB.connect()
        except OperationalError:
            LOGGER.error("Could not connect to database.")
            abort(503, "DB is not running.")
            
    @app.app.teardown_request
    def _close_db(exc):
        if not db_util.DB.is_closed():
            db_util.DB.close()

    LOGGER.info("created manager API")
    return app

app = create_app()