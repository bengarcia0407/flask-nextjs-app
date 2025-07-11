from flask import Flask, jsonify
from flask_cors import CORS
from models import db, User

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def index():
    return jsonify(message="Flask backend working!")

@app.route("/users")
def get_users():
    users = User.query.all()
    return jsonify(users=[u.name for u in users])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
