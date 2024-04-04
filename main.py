from flask import Flask
from flask import render_template



app = Flask(__name__)

@app.route("/")
def front_page():
    return render_template("./webpage.html")


if __name__ == "__main__":
    app.run()