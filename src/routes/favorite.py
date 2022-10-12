from flask import Blueprint, jsonify, request
from models import User, People, Planet, FavoritePeople, FavoritePlanet

bpFavorite = Blueprint('bpFavorite', __name__)

@bpFavorite.route('/favorite/planet/<int:planeta_id>', methods=['POST'])
def store_planet_by_user_id(planeta_id):
    new_fav_planet = FavoritePlanet()
    new_fav_planet.planet.id = planeta_id
    new_fav_planet.user_id= 1
    new_fav_planet.save()

    return jsonify({"message":"planet stored"}), 200


@bpFavorite.route('/favorite/people/<int:people_id>', methods=['POST'])
def store_people_by_user_id(people_id):
    new_fav_people = FavoritePeople()
    new_fav_people.people.id = people_id
    new_fav_people.user_id= 1
    new_fav_people.save()

    return jsonify({"message":"people stored"}), 200

@bpFavorite.route('/favorite/planet/<int:planeta_id>', methods=['DELETE'])
def delete_fav_planet(planeta_id):
    delete_fav_planet= FavoritePlanet.query.filter_by(user_id=1, planeta_id = planeta_id)
    delete_fav_planet.delete()

    return jsonify({"message":"planet deleted"}), 200

@bpFavorite.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_fav_people(people_id):
    delete_fav_people= FavoritePeople.query.filter_by(user_id=1, people_id = people_id)
    delete_fav_people.delete()

    return jsonify({"message":"people deleted"}), 200