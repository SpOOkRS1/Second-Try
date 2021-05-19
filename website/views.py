from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Maid, User
from . import db
import json
import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
  currentMonth = datetime.datetime.now()
  thisMonth = currentMonth.strftime("%B")
  return render_template("home.html", user=current_user, mquery=Maid.query.all(), thisMonth = thisMonth)

@views.route('/announcements')
def ATTN():
  currentMonth = datetime.datetime.now()
  thisMonth = currentMonth.strftime("%B")
  currentDate = datetime.datetime.now()
  currDate = currentDate.strftime("%b, %d")
  return render_template("announ.html", user=current_user, annList=User.query.all(), thisMonth = thisMonth, currDate = currDate)

@views.route('/add', methods=['GET', 'POST', 'DELETE'])
@login_required
def add():
    currentMonth = datetime.datetime.now()
    thisMonth = currentMonth.strftime("%B")
    if request.method == 'POST':
      maid = request.form.get('maid')
      chore = request.form.get('chore')

      if len(chore) < 1:
        flash('Chore is too short!', category='error')
        
      if len(maid) < 1:
        flash('Maid name is too short!', category='error')
      
      else:
        newMaid = Maid(maid=maid,chore=chore)
        db.session.add(newMaid)
        db.session.commit()

    return render_template("add.html", user=current_user, mquery=Maid.query.all(), thisMonth = thisMonth)


@views.route('/create', methods=['GET', 'POST', 'DELETE'])
@login_required
def create():
    currentMonth = datetime.datetime.now()
    thisMonth = currentMonth.strftime("%B")
    currentDate = datetime.datetime.now()
    currDate = currentDate.strftime("%b, %d")
    if request.method == 'POST':
      announcement = request.form.get('announcement')

      if len(announcement) < 1:
        flash('Chore is too short!', category='error')
      
      else:
        newAnn = User(announcement=announcement)
        db.session.add(newAnn)
        db.session.commit()

    return render_template("createAnnoun.html", user=current_user, annList=User.query.all(), thisMonth = thisMonth, currDate = currDate)


@views.route('/clear', methods=['GET', 'POST', 'DELETE'])
def clearTable():
  if request.method == 'POST':
    Maid.query.delete()
    db.session.commit()
    return redirect(url_for('views.add'))
  return render_template('clear.html', flash="Table was cleared.",mquery=Maid.query.all())