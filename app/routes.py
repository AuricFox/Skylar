from flask import request, render_template
from . import utils
from . import database
from flask import current_app as app


LOGGER = utils.LOGGER

# ====================================================================
# Main Pages
# ====================================================================
@app.route("/")
@app.route("/index")
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
        data['query'] = query

    data['tables'] = database.get_tables()

    return render_template('home.html', data=data)

# ====================================================================
# Custom page not found
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404