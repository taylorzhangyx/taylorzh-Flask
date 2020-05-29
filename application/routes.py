from application import app, db, api
from flask import (
    render_template,
    request,
    Response,
    json,
    jsonify,
    redirect,
    flash,
    url_for,
    session,
)
from flask_restx import Resource


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    logged_in = session.get("email")
    return render_template("index.html", index=True, logged_in=logged_in)
