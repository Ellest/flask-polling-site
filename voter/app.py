from flask import (
	Flask, render_template, request, flash, redirect, url_for, session
)
# security module
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

# create Flask obj and assign it to a variable
app = Flask(__name__)

#load config
app.config.from_object('config')

# initialize and create the DB
db.init_app(app)
db.create_all(app=app)

# route main page
@app.route('/')
def home():
	return render_template('cover.html')

# cover page
@app.route('/cover')
def cover():
	return render_template('cover.html')

@app.route('/logout')
def logout():
	pass

# signup page. methods outlines which request methods the page supports
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	# if post request -> signup
	if request.method == 'POST':

		# Need to make sure these fields exist, or accessing fields this way
		# will result in the Flask app failing with a 400 bad request error.
		# Might need to wrap it in a try except block to handle errors
		email = request.form['email']
		username = request.form['username']
		pw = request.form['password']

		pw = generate_password_hash(pw)

		user_obj = User(email=email, username=username, password=pw)

		# add status change
		db.session.add(user_obj)
		# commit change to database
		db.session.commit()

		# this stores the message at the end of the request and makes the message
		# available on the next request only.
		flash('Thanks for joining us. Please login with your credentials.')

		# dynamically gets the routed page for 'home'
		return redirect(url_for('home'))

	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_confirm():
	"""
	# Note: 
	#	Accessing this page with a request type not included in the methods argument
	#	will request in a bad request error. Thus we don't need to check and handle 
	# 	specifically for 'POST' requests in this case.
	"""
	username = request.form(['username'])
	pw = request.form('password')

	# querying the DB to get the user obj specified by the username
	# Getting first will return the right result as we've specified
	# a unique constraint on the username column.
	user = Users.query.filter_by(username=username).first()

	if user:
		pw_hash = user.password

		# check password and add user obj to session variable if credentials are valid
		if check_password_hash(password_hash, password):

			session['user'] = username

			flash('Login successful. Welcome.')

		return redirect(url_for('home'))
	else:

		# second argument indicates error?
		flash('Invalid credentials... Please try again.', 'error')

		return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()