import os

# path to the db file
DB_PATH = os.path.join(os.path.dirname(__file__), 'voter.db')
SECRET_KEY = 'dev key' # this needs to be private in a production setting
# DB URI for our DB
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)

# configurations
SQLALCHEMY_TRACKMODIFICATIONS =  False
DEBUG = True