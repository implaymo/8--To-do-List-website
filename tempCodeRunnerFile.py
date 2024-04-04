from flask import Flask
from flask import render_template
from forms import ToDoForm


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def front_page():
    form = ToDoForm()
    return render_template("webpage.html", form=form)


if __name__ == "__main__":
    app.run()