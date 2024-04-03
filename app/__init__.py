from flask import Flask
from . import database

from flask import Flask, render_template
import logging, os

PATH = os.path.dirname(os.path.abspath(__file__))

# Configure the logging object
logging.basicConfig(
    filename=os.path.join(PATH, '../logs/app.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)

LOGGER = logging.getLogger(__name__)

def init_app():
    '''
    Initializes the flask application

    Parameter(s): None

    Output(s):
        app (Object): flask application object
    '''
    app = Flask(__name__, instance_relative_config=False)
    # Configured for development
    app.config.from_object('config.DevConfig')

    # Initialized default database
    database.init_database()

    # Custom page not found
    def page_not_found(error):
        return render_template('404.html'), 404

    with app.app_context():
        # Import routes and custom modules
        from app.main import bp as main_bp
        from . import utils

        # Register blueprint to link routes
        app.register_blueprint(main_bp)
        app.register_error_handler(404, page_not_found)

    return app