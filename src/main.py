"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db

from routes.user import bpUser
from routes.people import bpPeople
from routes.planet import bpPlanet
from routes.specie import bpSpecie
from routes.favorite import bpFavorite

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


app.register_blueprint(bpUser, url_prefix='/api')
app.register_blueprint(bpPeople, url_prefix='/api')
app.register_blueprint(bpPlanet, url_prefix='/api')
app.register_blueprint(bpSpecie, url_prefix='/api')
app.register_blueprint(bpFavorite, url_prefix='/api')

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/home", methods=["GET"])
def handle_hello():

    response_body ={
        "msg": "This is your GET response"
    }

    return jsonify(response_body), 200

# @app.route('/users/favorites', methods=['GET'])
# def all_users_with_favorites():
#     users = User.query.all()
#     users = list(map(lambda user: user.serialize_with_favorites(), users))
#     return jsonify(users), 200

# @app.route('/users/favorites/people', methods=['GET'])
# def all_users_with_favorites_with_people():
#     users = User.query.all()
#     users = list(map(lambda user: user.serialize_with_favorites_with_contacts(), users))
#     return jsonify(users), 200

# @app.route('/users/favorites/planets', methods=['GET'])
# def all_users_with_favorites_with_planets():
#     users = User.query.all()
#     users = list(map(lambda user: user.serialize_with_favorites_with_planets(), users))
#     return jsonify(users), 200

# @app.route('/people', methods=['GET'])
# def all_people():
#     people = Planet.query.all()
#     people = list(map(lambda people: people.serialize(), people))
#     return jsonify(people), 200


# @app.route('/people/<int:id>', methods=['GET'])
# def get_people_by_id(id):
#     people = People.query.get(id)
#     return jsonify(people.serialize()), 200

# @app.route('/planets', methods=['GET'])
# def all_planets():
#     planets = Planet.query.all()
#     planets = list(map(lambda planets: planets.serialize(), planets))
#     return jsonify(planets), 200


# @app.route('/planets/<int:id>', methods=['GET'])
# def get_planet_by_id(id):
#     planet = Planet.query.get(id)
#     return jsonify(planet.serialize()), 200

# @app.route('/species', methods=['GET'])
# def all_species():
#     species = Specie.query.all()
#     species = list(map(lambda species: species.serialize(), species))
#     return jsonify(species), 200


# @app.route('/species/<int:id>', methods=['GET'])
# def get_specie_by_id(id):
#     specie = specie.query.get(id)
#     return jsonify(specie.serialize()), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
