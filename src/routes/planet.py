from flask import Blueprint, jsonify, request
from models import User, Planet

bpPlanet = Blueprint('bpPlanet', __name__)

@bpPlanet.route('/planets', methods=['GET'])
def all_planets():
    planets = Planet.query.all()
    planets = list(map(lambda planets: planets.serialize(), planets))
    return jsonify(planets), 200


@bpPlanet.route('/planets/<int:id>', methods=['GET'])
def get_planet_by_id(id):
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()), 200

