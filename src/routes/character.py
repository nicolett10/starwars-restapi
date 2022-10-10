from flask import Blueprint, jsonify, request
from models import User, Character

bpCharacter = Blueprint('bpCharacter', __name__)

@bpCharacter.route('/characters', methods=['GET'])
def all_characters():
    characters = Planet.query.all()
    characters = list(map(lambda characters: characters.serialize(), characters))
    return jsonify(characters), 200


@bpCharacter.route('/characters/<int:id>', methods=['GET'])
def get_character_by_id(id):
    character = Character.query.get(id)
    return jsonify(character.serialize()), 200