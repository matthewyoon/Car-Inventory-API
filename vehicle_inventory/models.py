from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash #check_password_hash for use in routes later

# Import for Secrets Module (Provided by Python)
import secrets #Generate public and private keys

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String, primary_key = True) #VarChar
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = False, default = '')
    token = db.Column(db.String, default = '', unique = True) # Unique means that each token needs to be different every time
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    
    def __init__(self,email,first_name = '', last_name = '', id = '', password = '', token = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)

    def set_token(self,length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'Your username/email: {self.email} has been created and added to database!'
