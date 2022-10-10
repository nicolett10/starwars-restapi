from flask import Blueprint, jsonify, request
from models import User, Specie

bpSpecie = Blueprint('bpSpecie', __name__)

@bpSpecie.route('/species', methods=['GET'])
def all_species():
    species = Specie.query.all()
    species = list(map(lambda species: species.serialize(), species))
    return jsonify(species), 200


@bpSpecie.route('/species/<int:id>', methods=['GET'])
def get_specie_by_id(id):
    specie = specie.query.get(id)
    return jsonify(specie.serialize()), 200