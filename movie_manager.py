import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "moviedatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
# db.create_all()
class Movie(db.Model):
    name = db.Column(db.String(80), nullable=False, primary_key=True)
    location = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "<Title: {}>".format(self.title)
