from flask import (
	Flask, render_template, request, flash, redirect, url_for, session
)
from werkzeug.security import generate_password_hash, check_password_hash
from models import db

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
	return render_template('index.html')

@app.route('/cover')
def cover():
	return render_template('cover.html')

if __name__ == '__main__':
	app.run()