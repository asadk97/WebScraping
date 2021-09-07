from flask import (Flask, render_template, abort, jsonify, request,
                   redirect, url_for)
from model import db, save_db

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template(
        "homepage.html",
        cards=db
    )


@app.route("/api/card/")
def api_card_list():
    return jsonify(db)


@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)
