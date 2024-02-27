from flask import Flask, request, render_template

import sys

sys.path.append('./src/')
import utils, database

LOGGER = utils.LOGGER

app = Flask(__name__, static_folder='static')
app.secret_key = 'my_super_secret_totaly_unbreakable_key'

# ====================================================================
@app.before_first_request
def before_first_request_func():
    '''
    Initialize the database for each new session
    '''
    database.init_database()

# ====================================================================
# Main Pages
# ====================================================================
@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home():
    '''
    Processes home page

    Parameter(s): None

    Output(s):
        A rendered HTML page with load db schema and data table if a POST is made
    '''
    data = {}

    if request.method == 'POST':
        
        query = request.form.get('code', type=str)
        data = database.db_query(query=query)

    data['tables'] = database.get_tables()

    return render_template('home.html', data=data)

# ====================================================================
# Custom page not found
'''@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404'''

# ====================================================================
# Run Main
# ====================================================================
if __name__ == "__main__":
    app.run()