from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    print("Uruchamiam aplikację Flask...")
    app.run(host="0.0.0.0", port=5000)

