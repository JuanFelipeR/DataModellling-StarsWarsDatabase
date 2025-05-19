from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

# Modelo de Usuario
class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    favorites_characters = relationship("FavoriteCharacter", backref="user")
    favorites_planets = relationship("FavoritePlanet", backref="user")
    favorites_vehicles = relationship("FavoriteVehicle", backref="user")

# Modelo de Personaje
class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    gender: Mapped[str] = mapped_column(String(20))
    birth_year: Mapped[str] = mapped_column(String(20))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=True)

    planet = relationship("Planet", backref="residents")

# Modelo de Planeta
class Planet(db.Model):
    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    climate: Mapped[str] = mapped_column(String(50))
    population: Mapped[int] = mapped_column(nullable=True)

# Modelo de Vehículo
class Vehicle(db.Model):
    __tablename__ = "vehicle"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50))
    passengers: Mapped[int] = mapped_column(nullable=True)
    pilot_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=True)

    pilot = relationship("Character", backref="vehicles")

# Modelo de Favoritos (uno para cada tipo, para simplificar)
class FavoriteCharacter(db.Model):
    __tablename__ = "favorite_character"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)

    character = relationship("Character")

class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)

    planet = relationship("Planet")

class FavoriteVehicle(db.Model):
    __tablename__ = "favorite_vehicle"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicle.id"), nullable=False)

    vehicle = relationship("Vehicle")
