from flask import Flask, request
from flask import render_template, redirect, url_for
from forms import ToDoForm, CheckmarkForm
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

# Create Database Table
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String)
    done = db.Column(db.Boolean)

# Route for the main page of the website
@app.route("/", methods=["GET","POST"])
def front_page():
    form = ToDoForm()
    checkmark = CheckmarkForm()
    if request.method == "POST":
        task = Tasks(task = form.input.data,
                    done = False)
        db.session.add(task)
        db.session.commit()
        # Clears input
        form.input.data = '' 
        return redirect(url_for("front_page"))
    
    all_tasks = Tasks.query.all()

    return render_template("webpage.html", form=form, all_tasks=all_tasks, checkmark=checkmark)




if __name__ == "__main__":
    app.run(debug=True)