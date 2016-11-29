from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.sqlalchemy import SQLAlchemy

from app import app

# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

from app.Modules.Auth.routing import *

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/Modules/Auth/db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True