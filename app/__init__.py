from flask import Flask
from . import database

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

    # Initialized default database
    database.init_database()

    with app.app_context():
        # Include routes
        from . import routes
        from . import utils
        

    return app