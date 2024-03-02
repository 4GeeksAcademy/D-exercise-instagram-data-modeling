import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="user")
    post = relationship("Post", back_populates="user")
    close_friends = relationship("CloseFriends", back_populates="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorites")
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorites")
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }

class CloseFriends(Base):
    __tablename__ = 'close friends'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorites")
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title
        }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
