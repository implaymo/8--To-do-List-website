from flask import Flask, request, redirect, url_for
from flask import render_template
from forms import ToDoForm
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
all_forms = []

@app.route("/", methods=["GET","POST"])
def front_page():
    form = ToDoForm()
    if form.validate_on_submit():
        all_forms.append(form)
        return render_template("webpage.html", form=form)
    return render_template("webpage.html", form=form)




if __name__ == "__main__":
    app.run(debug=True)