from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request
# from flask_bootstrap import Bootstrap5
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Report
from . import db
import json


auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		# search for the first instance of email in db
		user = User.query.filter_by(email=email).first()

		# if email exists in the db
		if user:
			# if user exists and passwords match
			if check_password_hash(user.password, password):
				message = 'Congratulations! You have successfully logged into your account.'
				flash(message, category='success')

				# loggin in the user
				login_user(user, remember=True)
				return redirect(url_for('views.index'))

			# if user exists and passwords do not match
			elif not check_password_hash(user.password, password):
				message = 'Oops! It looks like the password you entered is incorrect.Please check and try again.'
				flash(message, category='danger')

		# if user does not exists
		else:
			message = 'Oops! It looks like you do not have an account. Try signing up instead?'
			flash(message, category='danger')

	return render_template('login.html', user=current_user)

@auth.route('signup', methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		# get back data from the form
		username = request.form.get('username')
		email = request.form.get('email')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		# see if the user is already in the database
		user = User.query.filter_by(email=email).first()

		# validate data inputted into form
		if user:
			message = 'User already exists!'
			flash(message, category='danger')
		elif len(email) < 10 or len(username) < 1 or len(password1) < 5:
			message = 'Oops! It looks like you either entered an invalid email, username or password. Please check and try again.'
			flash(message, category='danger')
		elif password1 != password2:
			message = 'Your passwords do not match'
			flash(message, category='danger')
		else:
			message = 'Congratulations! You have created an account successfully'
			flash(message, category='success')

			# add the new user to the db
			new_user = User(email=email, username=username, password=generate_password_hash(password1))
			db.session.add(new_user)
			db.session.commit()

			# loggin session for new user
			login_user(new_user)
			return redirect(url_for('views.index'))

	return render_template('signup.html', user=current_user)

@auth.route('logout')
@login_required
def logout():
	logout_user()

	message = 'Oops! It looks like you have logged out of your account. Try logging back in?'
	flash(message, category='danger')
	return redirect(url_for('auth.login'))
