from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")

app.config["SECRET_KEY"] = getenv("SECRET_KEY")


db = SQLAlchemy(app)

from application import routes