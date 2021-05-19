from flask import Blueprint, render_template, request, flash, jsonify
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

@views.route('/add', methods=['GET', 'POST'])
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


@views.route('/delete-chore', methods=['POST'])
def delete_note():
    chore = json.loads(request.data)
    choreId = chore['choreId']
    chore = Maid.query.get(choreId)
    if chore:
        if chore.user_id == current_user.id:
            db.session.delete(chore)
            db.session.commit()
    return jsonify({})