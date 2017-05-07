from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

# creates a variable named db containing a new usable instance
# of the SQLAlchemy class:
db = SQLAlchemy()

# class to model the user's attrubutes
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True) #  constructor
  pwdhash = db.Column(db.String(54)) # sets a salted password

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     

  # set_password relies on the function generate_password_hash
  # which is a security function for importing from one of
  # Flask's libraries, werkzeug.    
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)