from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    favoriteplanets = db.relationship('FavoritePlanet', cascade="all, delete", backref="user")
    favoritecharacters = db.relationship('FavoriteCharacter', cascade="all, delete", backref="user")


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "active": self.active
        }

    # def serialize_with_agendas(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "active": self.active,
    #         "agendas": [agenda.serialize() for agenda in self.agendas]
    #     }

    # def serialize_with_agendas_with_contacts(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "active": self.active,
    #         "agendas": [agenda.serialize_with_contacts() for agenda in self.agendas]
    #     }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class FavoriteCharacter(db.Model):
    __tablename__ = 'favoritecharacters'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id', ondelete='CASCADE'), nullable=False)
    character = db.relationship('Character', cascade="all, delete")

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name
               }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class FavoritePlanet(db.Model):
    __tablename__ = 'favoriteplanets'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id', ondelete='CASCADE'), nullable=False)
    planet = db.relationship('Planet', cascade="all, delete", backref="user")

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name
               }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    films = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    starships = db.Column(db.String(100), nullable=False)
    role_by = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.String(100), nullable=False)
    eye_color = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    hair_color = db.Column(db.String(100), nullable=False)
    height = db.Column(db.String(100), nullable=False)
    homeworld = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.String(100), nullable=False)
    skin_color = db.Column(db.String(100), nullable=False)
    homeworld = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.String(100), nullable=False)
    skin_color = db.Column(db.String(100), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey(
        'planets.id', ondelete='CASCADE'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey(
        'species.id', ondelete='CASCADE'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "films": self.films,
            "name": self.name,
            "species": self.species,
            "starships": self.starships,
            "role_by": self.role_by,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "skin_color": self.skin_color
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    diameter = db.Column(db.String(20), nullable=False)
    rotation_period = db.Column(db.String(100), nullable=False)
    gravity = db.Column(db.String(100), nullable=False)
    population = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100), nullable=False)
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Specie(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    classification = db.Column(db.String(20), nullable=False)
    designation = db.Column(db.String(20), nullable=False)
    average_height = db.Column(db.String(20), nullable=False)
    average_lifespan = db.Column(db.String(20), nullable=False)
    eye_colors = db.Column(db.String(20), nullable=False)
    hair_colors = db.Column(db.String(20), nullable=False)
    skin_colors = db.Column(db.String(20), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    homeworld = db.Column(db.String(20), nullable=False)
    people = db.Column(db.String(20), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "average_height": self.average_height,
            "average_lifespan": self.average_lifespan,
            "eye_colors": self.eye_colors,
            "hair_colors": self.hair_colors,
            "skin_colors": self.skin_colors,
            "language": self.language,
            "homeworld": self.homeworld,
            "people": self.people,
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()