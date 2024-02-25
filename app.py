from flask import Flask, request, render_template, url_for, flash

import os
import sys

sys.path.append('./src/')
import utils

LOGGER = utils.LOGGER

app = Flask(__name__, static_folder='static')
app.secret_key = 'my_super_secret_totaly_unbreakable_key'

# ====================================================================
# Main Pages
# ====================================================================

@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template('home.html')

# Custom page not found
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404

# ====================================================================
# Run Main
# ====================================================================
if __name__ == "__main__":
    app.run()