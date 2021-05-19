from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import datetime

auth = Blueprint('auth', __name__)


@auth.route('/adlogin', methods=['GET', 'POST'])
def adlogin():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		user = User.query.filter_by(email=email).first()
		if user:
			if check_password_hash(user.password, password):
				flash('Logged in successfully!', category='success')
				login_user(user, remember=True)
				return redirect(url_for('views.home'))
			else:
				flash('Inncorrect password', category='error')
		else:
			flash('Email does not exist', category='error')
	return render_template('adlogin.html', user=current_user)


@auth.route('/adlogout')
@login_required
def adlogout():
	logout_user()
	return redirect(url_for('views.home'))


@auth.route('/adsign-up', methods=['GET', 'POST'])
def adsign_up():
	if request.method == 'POST':
		email = request.form.get('email')
		firstName = request.form.get('firstName')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		user = User.query.filter_by(email=email).first()
		if user:
			flash('Email already exists', category='error')
		elif len(email) < 4:
			flash('Email must be longer than 3 characters.', category='error')
		elif len(firstName) < 2:
			flash('Firstname must be longer than 1 character.',
			      category='error')
		elif password1 != password2:
			flash('Passwords do not match.', category='error')
		elif len(password1) < 7:
			flash('Password must be longer than 6 characters.',
			      category='error')
		else:
			# add user to the data base
			new_user = User(email=email,
			                firstName=firstName,
			                password=generate_password_hash(password1,
			                                                method='sha256'))
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user, remember=True)
			flash('Account created!', category='success')
			return redirect(url_for('views.home'))

	return render_template('adsign_up.html', user=current_user)
