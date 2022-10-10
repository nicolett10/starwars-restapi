from flask import Blueprint, jsonify, request
from models import User, Agenda

bpUser = Blueprint('bpUser', __name__)

@bpUser.route('/users', methods=['GET'])
def all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200

@bpUser.route('/users/agendas', methods=['GET'])
def all_users_with_agendas():
    users = User.query.all()
    users = list(map(lambda user: user.serialize_with_agendas(), users))
    return jsonify(users), 200

@bpUser.route('/users/agendas/contacts', methods=['GET'])
def all_users_with_agendas_with_contacts():
    users = User.query.all()
    users = list(map(lambda user: user.serialize_with_agendas_with_contacts(), users))
    return jsonify(users), 200

@bpUser.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    return jsonify(user.serialize()), 200

@bpUser.route('/users/<int:id>/agendas', methods=['GET'])
def get_user_by_id_with_agendas(id):
    user = User.query.get(id)
    return jsonify(user.serialize_with_agendas()), 200

@bpUser.route('/users/<int:id>/agendas', methods=['POST'])
def store_agenda_by_user_id(id):
    user = User.query.get(id)

    title = request.json.get('title')

    """ agenda = Agenda()
    agenda.title = title
    agenda.users_id = user.id
    agenda.save() """

    agenda = Agenda()
    agenda.title = title
    user.agendas.append(agenda)
    user.update()

    return jsonify(user.serialize_with_agendas()), 200

@bpUser.route('/users/<int:id>/agendas/contacts', methods=['GET'])
def get_user_by_id_with_agendas_with_contacts(id):
    user = User.query.get(id)
    return jsonify(user.serialize_with_agendas_with_contacts()), 200


@bpUser.route('/users/<int:id>/agendas/<int:agendas_id>/contacts', methods=['GET'])
def get_user_by_id_with_agenda_by_id_with_contacts(id, agendas_id):
    agenda = Agenda.query.filter_by(users_id=id, id=agendas_id).first()
    return jsonify(agenda.serialize_with_contacts()), 200