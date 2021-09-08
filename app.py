from flask import (Flask, render_template, request,)
# from model import db, save_db
import main_task

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template(
            "index.html"
    )
    else:
        url = request.form.get("user_input")
        soup = main_task.get_content(url)
        return render_template("results.html", output=soup)


@app.route("/results")
def results():
    return render_template(
        "results.html"
    )