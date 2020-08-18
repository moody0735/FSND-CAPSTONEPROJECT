import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "capstone"
database_path = "postgres://{}:{}@{}/{}".format('postgres', '9520099', 'localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    return db





# ---------------------------------------------------------
# Models.
# ---------------------------------------------------------

class Actor(db.Model):
    __tablename__ = 'actor'
    # Autoincrementing, unique primary key
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

  
    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

  
    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())



class Movie(db.Model):
    __tablename__ = 'movie'
    # Autoincrementing, unique primary key
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release =  Column(Integer)



    def __init__(self, title, release):
        self.title = title
        self.release = release 


  
    def short_movie(self):
        return {
            'id': self.id,
            'title': self.title
        }

  
    def long_movie(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short_movie())