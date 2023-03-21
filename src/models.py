import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


favorite_characters = Table(
    "favorite_characters",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("character_id", ForeignKey("characters.id")),
)

favorite_planets = Table(
    "favorite_planets",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("planet_id", ForeignKey("planets.id")),
)

favorite_starships = Table(
    "favorite_starships",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("starship_id", ForeignKey("starships.id")),
)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(120), unique=False, nullable=False)
    last_name = Column(String(120), unique=False, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    favorite_characters = relationship('Characters', secondary="favorite_characters")
    favorite_planets = relationship('Planets', secondary="favorite_planets")
    favorite_starships = relationship('Starships', secondary="favorite_starships")
   
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "list_favorites": list(map(lambda x: x.serialize(), self.list_favorites)),
            # do not serialize the password, its a security breach

        }


class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name= Column(String(120), unique=True, nullable=False)
    description = Column(String(550), unique=False, nullable=False)
    image_link = Column(String(550), unique=False, nullable=False)
    # user_id = Column(Integer, ForeignKey("user.id"))
    # user = relationship("User", back_populates="favorites")

    def __repr__(self):
        return f'<Characters {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # "ingredients": list(map(lambda x: x.serialize(), self.ingredients)),
            # do not serialize the password, its a security breach
        }



class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name= Column(String(120), unique=True, nullable=False)
    description = Column(String(550), unique=False, nullable=False)
    image_link = Column(String(550), unique=False, nullable=False)
    # user_id = Column(Integer, ForeignKey("user.id"))
    # user = relationship("User", back_populates="favorites")

    def __repr__(self):
        return f'<Planets {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_link": self.image_link
            # do not serialize the password, its a security breach
        }

class Starships(Base):
    __tablename__ = "starships"
    id = Column(Integer, primary_key=True)
    name= Column(String(120), unique=True, nullable=False)
    description = Column(String(550), unique=False, nullable=False)
    image_link = Column(String(550), unique=False, nullable=False)
    # user_id = Column(Integer, ForeignKey("user.id"))
    # user = relationship("User", back_populates="favorites")

    def __repr__(self):
        return f'<Starships {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_link": self.image_link
            # do not serialize the password, its a security breach
        }



        

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
