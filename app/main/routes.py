from flask import render_template, request
from app.main import bp
from app import database

# ====================================================================
# Main Pages
# ====================================================================
@bp.route("/")
@bp.route("/index")
@bp.route("/home", methods=["POST", "GET"])
def index():
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
# Custom favicon
@bp.route('/favicon.ico')
def favicon():
    return bp.send_static_file('images/favicon.ico')