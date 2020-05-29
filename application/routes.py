from application import app
from flask import (
    render_template,
    request,
    Response,
    json,
    jsonify,
    redirect,
    flash,
    url_for,
)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    return render_template("index.html")
