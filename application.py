import os

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)


class Repos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    language = db.Column(db.String)
    stars = db.Column(db.Integer)
    forks = db.Column(db.Integer)
    date = db.Column(db.String)

    def asdict(self):
        return {
            "id": self.id,
            "name": self.name,
            "language": self.language,
            "stars": self.stars,
            "forks": self.forks,
            "date": self.date
        }


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/data", methods=["GET", "POST"])
def data():

    if request.method == "POST":

        item = request.get_json()

        new_repo = Repos(name=item["name"], language=item["language"],
                         stars=item["stargazers_count"], forks=item["forks_count"], date=item["date"])

        db.session.add(new_repo)
        db.session.commit()

        return "Stored to database: " + item["name"]

    else:

        repo_array = []

        all_repos = Repos.query.order_by(Repos.id).all()

        for repo in all_repos:
            
            repo_array.append(repo.asdict())

        return jsonify(repo_array)


if __name__ == "__main__":
    app.run(debug=True)
