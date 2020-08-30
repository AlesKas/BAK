import os
import connexion

from connexion.resolver import RestyResolver

def create_app():
    app = connexion.App("Network attached storage", options={'swagger_ui': True})
    app.app.url_map.strict_slashes = False
    app.add_api('manager.specs.yaml',
                resolver=RestyResolver('api'),
                validate_responses=True,
                strict_validation=True)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)