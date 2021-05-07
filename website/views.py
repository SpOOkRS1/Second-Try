from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Chore, Maid
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
  
  return render_template("home.html", user=current_user, cquery=Chore.query.all(), mquery=Maid.query.all())

@views.route('/adchore', methods=['GET', 'POST'])
@login_required
def adchore():
    if request.method == 'POST':
        chore = request.form.get('chore')

        if len(chore) < 1:
            flash('Chore is too short!', category='error')
        else:
            new_chore = Chore(chore=chore)
            db.session.add(new_chore)
            db.session.commit()
            flash('Chore added!', category='success')

    return render_template("adchore.html", user=current_user, cquery=Chore.query.all())

@views.route('/admaid', methods=['GET', 'POST'])
@login_required
def admaid():
    if request.method == 'POST':
        maid = request.form.get('maid')

        if len(maid) < 1:
            flash('Maid name is too short!', category='error')
        else:
            new_maid = Maid(maid=maid)
            db.session.add(new_maid)
            db.session.commit()
            flash('Maid added!', category='success')

    return render_template("admaid.html", user=current_user, mquery=Maid.query.all())


@views.route('/delete-chore', methods=['POST'])
def delete_note():
    chore = json.loads(request.data)
    choreId = chore['choreId']
    chore = Chore.query.get(choreId)
    if chore:
        if chore.user_id == current_user.id:
            db.session.delete(chore)
            db.session.commit()
    return jsonify({})