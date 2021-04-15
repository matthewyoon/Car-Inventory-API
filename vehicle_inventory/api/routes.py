from flask import Blueprint, request, jsonify
from vehicle_inventory.helpers import token_required
from vehicle_inventory.models import User, Vehicle, vehicle_schema, vehicles_schema, db

api = Blueprint('api', __name__, url_prefix='/api')

# @api.route('/getdata')
# def getdata():
#     return {'some': 'value'}


# create vehicle endpoint
@api.route('/vehicles', methods = ['POST'])
@token_required
def create_vehicle(current_user_token):
    vehicle_type = request.json['vehicle_type']
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    price = request.json['price']
    engine = request.json['engine']
    fuel = request.json['fuel']
    msrp = request.json['msrp']
    user_token = current_user_token.token

    vehicle = Vehicle(vehicle_type,make,model,year,color,price,engine,fuel,msrp,user_token = user_token)

    db.session.add(vehicle)
    db.session.commit()

    response = vehicle_schema.dump(vehicle)
    return jsonify(response) 


# retrieve all vehicles endpoint
@api.route('/vehicles', methods = ['GET'])
@token_required
def get_vehicles(current_user_token):
    owner = current_user_token.token
    vehicle = Vehicle.query.filter_by(user_token = owner).all()
    response = vehicles_schema.dump(vehicle)
    return jsonify(response)

# Retrieve one vehicle endpoint
@api.route('/vehicles/<id>', methods = ['GET'])
@token_required
def get_vehicle(current_user_token, id):
    vehicle = Vehicle.query.get(id)
    response = vehicle_schema.dump(vehicle)
    return jsonify(response)


# Update vehicle endpoint
@api.route('/vehicles/<id>', methods = ['POST', 'PUT'])
@token_required
def update_vehicle(current_user_token, id):
    vehicle = Vehicle.query.get(id) # Getting a vehicle instance

    vehicle.vehicle_type = request.json['vehicle_type']
    vehicle.make = request.json['make']
    vehicle.model = request.json['model']
    vehicle.year = request.json['year']
    vehicle.color = request.json['color']
    vehicle.price = request.json['price']
    vehicle.engine = request.json['engine']
    vehicle.fuel = request.json['fuel']
    vehicle.msrp = request.json['msrp']
    vehicle.user_token = current_user_token.token

    db.session.commit()
    response = vehicle_schema.dump(vehicle)
    return jsonify(response)


# Delete vehicle endpoint
@api.route('/vehicles/<id>', methods = ['DELETE'])
@token_required
def delete_vehicle(current_user_token, id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    response = vehicle_schema.dump(vehicle)
    return jsonify(response)
