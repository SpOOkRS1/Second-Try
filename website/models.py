from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  firstName = db.Column(db.String(150))
  announcement = db.Column(db.String(100000))

class Maid(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  maid = db.Column(db.String(100))
  chore = db.Column(db.String(100))

def __init__(self,maid,chore):
  self.maid = maid
  self.chore= chore
  
def __repr__(self):
  return (f"MAID: {self.maid}      CHORE:{self.chore}")