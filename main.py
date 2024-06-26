import threading

# import "packages" from flask
from flask import (
    Flask,
    render_template,
    request,
)  # import render_template from "public" flask libraries
from flask.cli import AppGroup
from flask_cors import CORS

# import "packages" from "this" project
from __init__ import app, db, cors  # Definitions initialization


# setup APIs
from api.titanic import titanic_api
from api.recognition import recognition_api

# database migrations
from model.titanics import initTitanic

# setup App pages
# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(titanic_api)
app.register_blueprint(recognition_api)


@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404


@app.route("/")  # connects default URL to index() function
def index():
    return render_template("index.html")


@app.route("/table/")  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")


@app.before_request
def before_request():
    # Check if the request came from a specific origin
    allowed_origin = request.headers.get("Origin")
    if allowed_origin in [
        "http://localhost:4100",
        "http://127.0.0.1:4100",
    ]:
        cors._origins = allowed_origin


# Create an AppGroup for custom commands
custom_cli = AppGroup("custom", help="Custom commands")


# Define a command to generate data
@custom_cli.command("generate_data")
def generate_data():
    initTitanic()


# Register the custom command group with the Flask application
app.cli.add_command(custom_cli)


# @app.before_first_request
def activate_job():
    initUsers()


# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    app.run(debug=True, host="0.0.0.0", port="8028")
