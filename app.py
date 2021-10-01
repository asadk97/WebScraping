import requests
from flask import (Flask, render_template, request,)
# from model import db, save_db
from main import main_task

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template(
            "index.html"
        )

    else:
        url = request.form.get("user_input")
        try:
            requests.get(url)
        except:
            soup = "Invalid URL please enter a valid URL"
            return render_template("results.html", output=soup)

        else:
            if requests.get(url).status_code == 200:
                soup = main_task.get_content(url)
                return render_template("results.html", output=soup)
            else:
                output = "Invalid URL please enter a valid URL"
                return render_template("results.html", output=output)


@app.route("/results")
def results():
    return render_template(
        "results.html"
    )
