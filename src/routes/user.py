from flask import Blueprint, jsonify, request
from models import User

bpUser = Blueprint('bpUser', __name__)

@bpUser.route('/users', methods=['GET'])
def all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200

@bpUser.route('/users/favorites', methods=['GET'])
def all_users_with_favorites():
    users = User.query.all()
    users = list(map(lambda user: user.serialize_with_favorites(), users))
    return jsonify(users), 200

