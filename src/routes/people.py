from flask import Blueprint, jsonify, request
from models import User, People

bpPeople = Blueprint('bpPeople', __name__)

@bpPeople.route('/people', methods=['GET'])
def all_people():
    people = People.query.all()
    people = list(map(lambda people: people.serialize(), people))
    return jsonify(people), 200


@bpPeople.route('/people/<int:id>', methods=['GET'])
def get_people_by_id(id):
    people = People.query.get(id)
    return jsonify(people.serialize()), 200