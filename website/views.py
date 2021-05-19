from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Maid
from . import db
import json
import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
  currentMonth = datetime.datetime.now()
  thisMonth = currentMonth.strftime("%B")
  return render_template("home.html", user=current_user, mquery=Maid.query.all(), thisMonth = thisMonth)

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


@views.route('/clear', methods=['GET', 'POST', 'DELETE'])
def clearTable():
  if request.method == 'POST':
    Maid.query.delete()
    db.session.commit()
    return redirect(url_for('views.add'))
  return render_template('clear.html', flash="Table was cleared.",mquery=Maid.query.all())