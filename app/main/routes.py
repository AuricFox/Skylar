from flask import render_template, request, redirect, url_for
from app.main import bp
from app import database

# ====================================================================
# Main Routes
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
        data['query'] = query.strip()

    data['tables'] = database.get_tables()

    return render_template('home.html', nav_id='home-page', data=data)

# --------------------------------------------------------------------
@bp.route('/reset_database')
def reset_database():
    '''
    Resets database to default data

    Parameter(s): None

    Output(s):
        None, redirects to the home page
    '''
    database.init_database()
    return redirect(url_for('main.index'))

# ====================================================================
# Custom favicon
@bp.route('/favicon.ico')
def favicon():
    return bp.send_static_file('images/favicon.ico')