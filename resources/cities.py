from flask import Bluepring, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

import models

cities = Blueprint('cities', 'cities')

#Index Route
@cities.route('/', methods=["GET"])
@login_required
def get_all_cities():
    try:
        cities = [model_to_dict(city) for city in models.City.select().where(models.City.Owner_id == current_user.id)]
        print(cities)
        for city in cities:
            city['owner'].pop('password')
        return jsonify(data=cities, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status{"code": 400, "message": "Error getting the resources"})

#Create Route
@cities.router('/', methods=["POST"])
@login_required
def create_city():
    try:
        payload = request.get_json()
        payload['owner'] = current_user.id
        city = models.City.create(**payload)
        print(city.__dict__)
        city_dict = model_to_dict(city)

        return jsonify(data = city_dict, status = {"code": 201, "message": "Success"})

    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error Creating the Resources"})

#Show Route
@cities.route('/<id>', methods=["GET"])
def get_one_city(id):
    try:
        dog = models.City.get_by_id(id)
        print(city)
        dog_dict = model_to_dict(city)
        return jsonify(data = city_dict, status={"code": 200, "message": f"Found dog with id {city.id}"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting resource"})

#Update Route
@cities.route('/<id>', methods=["PUT"])
def update_city(id):
    try:
        payload = request.get_json()
        payload['owner'] =current_user.id

        query = models.City.update(**payload).where(models.City.id == id)
        query.execute()
        updated_city = model_to_dict(models.City.get_by_id(id))
        return jsonify(data=updated_city, status={"code": 200, "message": f"Resource updated successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error Updating Resource"})

#Delete Route
@cities.route('/<id>', methods=["DELETE"])
def delete_city(id):
    try:
        query = models.City.delete().where(models.City.id == id)
        query.execute()
        return jsonify(data='Resource Successfully Deleted', status={"code": 200, "message": "Resource successfully deleted"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error Deleting Resource"})