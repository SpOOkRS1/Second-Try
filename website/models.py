from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime

class Chore(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  chore = db.Column(db.String(100))
  date = db.Column(db.DateTime(timezone=True), default=func.now())

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  firstName = db.Column(db.String(150))

class Maid(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  maid = db.Column(db.String(100))
