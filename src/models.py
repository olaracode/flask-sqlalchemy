import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    phone_number = Column(String(20))
    bio = Column(String(250))

    # Booleanos
    is_banned = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    # Relationships
    tweets = relationship("Tweet", backref="tweets") # Referencia a la relacion
    likes = relationship("Like", backref="user_likes")

    blocked = relationship("Blocked", backref="blocked_users")

class Tweet(Base):
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True)
    content = Column(String(255), nullable=False)
    # Datetime = Fecha y Hora
    published_at = Column(DateTime, default=datetime.now())

    # Relationship
    user_id = Column(Integer, ForeignKey("user.id"))
    likes = relationship("Like", backref="tweet_likes")

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    # Relationship
    tweet_id = Column(Integer, ForeignKey("tweet.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

class Blocked(Base):
    __tablename__ = "blocked"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    blocked_id = Column(Integer, ForeignKey("user.id"))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
