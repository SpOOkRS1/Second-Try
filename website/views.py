from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Maid, User, Announcement
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
def announcements():
  currentMonth = datetime.datetime.now()
  thisMonth = currentMonth.strftime("%B")
  currentDate = datetime.datetime.now()
  currDate = currentDate.strftime("%b, %d")
  
  return render_template("announcements.html", user=current_user, annList= Announcement.query.all(), thisMonth = thisMonth, currDate = currDate)

@views.route('/requirements')
def requirements():
  
  return render_template("requirements.html", user=current_user)

@views.route('/chores', methods=['GET', 'POST', 'DELETE'])
@login_required
def chores():
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

    return render_template("chores.html", user=current_user, mquery=Maid.query.all(), thisMonth = thisMonth)


@views.route('/announce', methods=['GET', 'POST', 'DELETE'])
@login_required
def announce():
    currentMonth = datetime.datetime.now()
    thisMonth = currentMonth.strftime("%B")
    currentDate = datetime.datetime.now()
    currDate = currentDate.strftime("%b, %d")
    if request.method == 'POST':
      announcement = request.form.get('announcement')

      if len(announcement) < 1:
        flash('Chore is too short!', category='error')
      
      else:
        newAnn = Announcement(announcement=announcement)
        db.session.add(newAnn)
        db.session.commit()

    return render_template("announce.html", user=current_user, annList=Announcement.query.all(), thisMonth = thisMonth, currDate = currDate)


@views.route('/clearch', methods=['GET', 'POST', 'DELETE'])
@login_required
def clearch():
  if request.method == 'POST':
    Maid.query.delete()
    db.session.commit()
    return redirect(url_for('views.chores'))
  return render_template('clearChores.html', flash="Table was cleared.",mquery=Maid.query.all())


@views.route('/clearan', methods=['GET', 'POST', 'DELETE'])
@login_required
def clearan():
  if request.method == 'POST':
    Announcement.query.delete()
    db.session.commit()
    return redirect(url_for('views.announce'))
  return render_template('clearAnnouncements.html', flash="Table was cleared.")