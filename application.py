import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/data", methods=["POST"])
def data():

	arguments = request.get_json()

	print(arguments["node_id"])

	return "Nothing for now"

if __name__ == "__main__":
    app.run(debug=True)