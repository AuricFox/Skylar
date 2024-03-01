from flask import Flask

def create_app():
    '''
    Initializes the flask application and database

    Parameter(s): None

    Output(s):
        app (Object): flask application object
    '''
    app = Flask(__name__, instance_relative_config=False)
    # Configure for development
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Include routes
        from . import routes
        from . import utils
        from . import database

    return app