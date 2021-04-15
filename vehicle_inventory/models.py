from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash #check_password_hash for use in routes later

# Import for Secrets Module (Provided by Python)
import secrets #Generate public and private keys

from flask_login import LoginManager, UserMixin

from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True) #VarChar
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = False, default = '')
    token = db.Column(db.String, default = '', unique = True) # Unique means that each token needs to be different every time
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    vehicle = db.relationship('Vehicle', backref = 'owner', lazy = True)
    
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

class Vehicle(db.Model):
    id = db.Column(db.String, primary_key = True)
    vehicle_type = db.Column(db.String(100))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Numeric(precision=4,scale=0))
    color = db.Column(db.String(100))
    price = db.Column(db.Numeric(precision=9, scale=2))
    engine = db.Column(db.String(100))
    fuel = db.Column(db.String(100))
    msrp = db.Column(db.Numeric(precision=9, scale=2))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, vehicle_type, make, model, year, color, price, engine, fuel, msrp, user_token, id = ''):
        self.id = self.set_id()
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.engine = engine
        self.fuel = fuel
        self.msrp = msrp
        self.user_token = user_token

    def __repr__(self):
        return f'The following vehicle has been added: {self.make} {self.model}.'

    def set_id(self):
        return secrets.token_urlsafe()

class VehicleSchema(ma.Schema):
    class Meta:
        fields = ['id','vehicle_type','make','model','year','color','price','engine','fuel','msrp']

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many = True)