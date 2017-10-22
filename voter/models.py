from flask_sqlalchemy import SQLAlchemy

# create SQL Alchemy obj
db = SQLAlchemy()

class Base(db.Model):
	"""
	Base class. Specific models will be derived off of this class.
	"""
	__abstract__ = True

	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
								onupdate=db.func.current_timestamp())

class Topics(Base):
	"""
	Model representing polling topics
	"""
	title = db.Column(db.String(500))

	# representation
	def __repr__(self):
		return self.title

class Options(Base):
	"""
	Model representing polling options
	"""
	name = db.Column(db.String(200))


class Polls(Base):
	"""
	Polls model. Derives from the base class.
	"""
	# model layout
	topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
	option_id = db.Column(db.Integer, db.ForeignKey('options.id'))
	votes = db.Column(db.Integer, default=0)
	status = db.Column(db.Boolean)

	# Foreing key constraint to Topics table.
	# Backref instantiates a bidirectional relationship between the options
	# model and polls model. Allows us to access properties in the other table
	# due to the bidirectional Object Relational Mapping
	topic = db.relationship('Topics', foreign_keys=[topic_id], 
							backref=db.backref('options',lazy='dynamic'))

	# foreign key constraint to Options table
	# foreign key column = option_id
	option = db.relationship('Options', foreign_keys=[option_id])

	# representation
	def __repr__(self):
		return self.option.name

class User(Base):
	"""
	User Model
	"""
	# setting unique constraints
	email = db.Column(db.String(100), unique=True)
	username = db.Column(db.String(50), unique=True)
	# this column will be the hash of the raw password
	# making it long enough to avoid truncation
	password = db.Column(db.String(200))