import os
from flask import Flask
from flask import render_template
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "moviedatabase.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
# db.create_all()
class Movie(db.Model):
    name = db.Column(db.String(80), nullable=False, primary_key=True)
    location = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "<Title: {}>".format(self.title)


@app.route("/", methods=["GET"])
def home():
        movies = Movie.query.all()
        return render_template("home.html", movies=movies)


@app.route("/update", methods=["GET", "Post"])
def update():
        movies = Movie.query.all()
        return render_template("update.html", movies=movies)

@app.route("/update_value", methods=["GET", "Post"])
def update_vale():
    name = request.args.get('name', None)
    movie = Movie.query.filter_by(name=name).first()
    return render_template("update_value.html", movie=movie)



@app.route("/input", methods=["GET", "POST"])
def input():

    if request.form:
        movie = Movie(name=request.form.get("name"),
                     location=request.form.get("location"),
                     time=request.form.get("time"), )
        db.session.add(movie)
        db.session.commit()
        movies = Movie.query.all()
        return render_template("home.html", movies=movies)
    else:
        movies = Movie.query.all()
        return render_template("input.html", movies=movies)


@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    movie = Movie.query.filter_by(name=name).first()
    db.session.delete(book)
    db.session.commit()
    return render_template("delete.html",movie=movie)

# @app.route("/update", methods=["POST"])
# def update():
#     newname = request.form.get("newname")
#     oldname = request.form.get("oldname")
#
#     newlanguage = request.form.get("newlanguage")
#     oldlanguage = request.form.get("oldlanguage")
#
#     newtime = request.form.get("newtime")
#     oldtime = request.form.get("oldtime")
#
#
#     book = Book.query.filter_by(title=oldtitle).first()
#     book.title = newtitle
#     db.session.commit()
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
