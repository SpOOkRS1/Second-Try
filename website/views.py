from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Chore
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
  
  return render_template("home.html", user=current_user)

@views.route('/adhome', methods=['GET', 'POST'])
@login_required
def adhome():
    if request.method == 'POST':
        chore = request.form.get('chore')

        if len(chore) < 1:
            flash('Chore is too short!', category='error')
        else:
            new_chore = Chore(data=chore, user_id=current_user.id)
            db.session.add(new_chore)
            db.session.commit()
            flash('Chore added!', category='success')

    return render_template("adhome.html", user=current_user)

@views.route('/admaid', methods=['GET', 'POST'])
@login_required
def admaid():
    if request.method == 'POST':
        maid = request.form.get('maid')

        if len(maid) < 1:
            flash('Maid name is too short!', category='error')
        else:
            new_maid = Chore(maid=maid, user_id=current_user.id)
            db.session.add(new_maid)
            db.session.commit()
            flash('Maid added!', category='success')

    return render_template("admaid.html", user=current_user)


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