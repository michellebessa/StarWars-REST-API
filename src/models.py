from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorites', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'Character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    height = db.Column(db.Integer(), unique=False, nullable=False)
    mass = db.Column(db.Integer(), unique=False, nullable=False)
    hair_color = db.Column(db.String(100), unique=True, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.Integer(), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    favorites_id = db.Column(db.Integer(), db.ForeignKey("Favorites.id"))


    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'Planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer(), unique=False, nullable=False)
    orbital_period = db.Column(db.Integer(), unique=False, nullable=False)
    diameter = db.Column(db.Integer(), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    surface_water = db.Column(db.Integer(), unique=False, nullable=False)
    population = db.Column(db.Integer(), unique=False, nullable=False)
    favorites_id = db.Column(db.Integer(), db.ForeignKey("Favorites.id"))


    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Vehicles(db.Model):
    __tablename__ = 'Vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    model = db.Column(db.Integer(), unique=False, nullable=False)
    manufacterer = db.Column(db.String(80), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer(), unique=False, nullable=False)
    length = db.Column(db.Integer(), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer(), unique=False, nullable=False)
    crew = db.Column(db.Integer(), unique=False, nullable=False)
    passengers = db.Column(db.Integer(), unique=False, nullable=False)
    cargo_capacity = db.Column(db.Integer(), unique=False, nullable=False)
    favorites_id = db.Column(db.Integer(), db.ForeignKey("Favorites.id"))


    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = 'Favorites'
    id = db.Column(db.Integer, primary_key=True)
    favorite_name = db.Column(db.String(80), unique=True, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("User.id"))
    character_id = db.relationship('Character', lazy=True)
    planets_id = db.relationship('Planets', lazy=True)
    vehicles_id = db.relationship('Vehicles', lazy=True)


    def __repr__(self):
        return '<Favorites %r>' % self.favorite_name

    def serialize(self):
        return {
            "id": self.id,
            "favorite_name": self.favorite_name,
            # do not serialize the password, its a security breach
        }