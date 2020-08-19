# Casting Agency
Udacity Fullstack Nanodegree capstone project

## Introduction
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 
 
The motivation of this project is to practice the skills learned during the Udacity FullStack NanoDegree program. The basis of the app for Casting Directors to be able to post their actors and movies.


# The Stack
* [Python 3.8.2](https://www.python.org/downloads/release/python-382/)  
* [Flask - Web Framework](https://flask.palletsprojects.com/en/1.1.x/)
* [SQLAlechmy ORM](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [PostgresSQL 12.2](https://www.postgresql.org/docs/12/release-12-2.html) 
* [Flask - Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* RESTful - API
* Authentication - JSON Web Token (JWT) with [Auth0](auth0.com)
* User Roles/Permissions
* Python virtual environment - [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* Python - [unittest](https://docs.python.org/3/library/unittest.html#module-unittest)
* Deployment on [Heroku](https://heroku.com/)


## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 




## Running the server

From within the `Capstone` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --reload
```



## Running the API 
API endpoints can be accessed via https://fsndheroku-agency.herokuapp.com/

## API Reference

## Getting Started
Base URL: This application can be run locally. The hosted version is at `https://fsndheroku-agency.herokuapp.com`.

Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root (or health) endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:
- Csting Assistant
  - can only view the list of artist and movies
  - has `get:actors, get:movies` permissions
- Casting Director
  - can perform all the actions that `Assistant` can
  - can also create an actor and also update respective information
  - has `patch:actor, patch:movie, post:actor, delete:actor` permissions in addition to all the permissions that `Assistant` role has
- Casting Producer
  - can perform all the actions that `Director` can
  - can also delete a movie
  - has `delete:movie, patch:movie` permissions in addition to all the permissions that `Director` role has


### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions above.


    

### API Documentation
# Endpoints and Error Handlers
Error Handling
Errors are returned in the following json format:

```
 "success": "False",
  "error": 422,
  "message": "unprocessable",
```
The error codes currently returned are:

- 401 – unathorized
- 404 – resource not found
- 422 – unprocessable




**ENDPONTS**

1. GET '/actors'
2. GET '/movies'
3. POST '/actors'
4. POST '/movies'
5. PATCH '/actors/<int:id>'
6. PATCH '/movies/<int:id>'
7. DELETE '/actors/<int:id>'
8. DELETE '/movies/<int:id>'

```bash
GET '/actors'
- No Authorization required
- Gets all the actors that are in the database
- Test: curl http://127.0.0.1:5000/actors Returns
    "actors": [
    {
      "age": 51,
      "gender": "Female",
      "id": 1,
      "name": "Jennifer Lopez"
    }
  ],
  "success": true
}



GET '/movies'
- No Authorization required
- Gets all the movies that are in the database
- curl http://127.0.0.1:5000/movies Returns
    "movies": [
    {
      "id": 1,
      "title": "Messages Not"
    },
    {
      "id": 2,
      "title": "NEW MOVIE ADDED"
    }
  ],
  "success": true
}




POST '/actors'
- Required Authorization with 'Casting Dorector' or 'Casting Producer' role
- Casting Director or Casting Producer can post actors
- curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type:application/json" -d '{"name": "Leonardo", "age": "45", "gender": "male"}' http://127.0.0.1:5000/actors
- Returns:
 
    {
        "create": 2,
        "status_code": 200,
        "success": true
    }


POST '/movies'
- Required Authorization with 'Casting Producer' role
- Casting Producer can post movies
- curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type:application/json" -d '{"title": "Room", "release": "2015"}' http://127.0.0.1:5000/movies
- Returns:
    {
        "create": 3,
        "status_code": 200,
        "success": true
    }


PATCH '/actors/<int:id>'
- Requred Authorization with 'Casting Dorector' or 'Casting Producer' role
- Casting Director or Casting Producer can patch actors. They can edit the name, the age, or gender
- curl -X PATCH -H "Authorization: Bearer <token>" -H "Content-Type:application/json" -d '{"age": "20"}' http://127.0.0.1:5000/movies/1
- Returns:
    {
        "status_code": 200,
        "success": True
    }



PATCH '/movies/<int:id>'
- Requred Authorization with 'Casting Producer' role
- Casting Producer can patch movies. They can edit the title, or release
- curl -X PATCH -H "Authorization: Bearer <token>" -H "Content-Type:application/json" -d '{"title": "Messages Not"}' http://127.0.0.1:5000/movies/1
- Returns:
    {
        "status_code": 200,
        "success": True
    }

DELETE '/actors/<int:id>'
- Requred Authorization with 'Casting Dorector' or 'Casting Producer' role
- Deletes the actor with id replaced by <int:id>
- curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer <token>" http://127.0.0.1:5000/actors/1
- Returns Response if deletes succesfully:
    {
        "delete": 1,
        "success": true
    }


DELETE '/movies/<int:id>'
- Requred Authorization with 'Casting Producer' role
- Deletes the movie with id replaced by <int:id>
- curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer <token>" http://127.0.0.1:5000/movies/1
- Returns Response if deletes succesfully:
    {
        "delete": 1,
        "success": true
    }
```


### Unittesting
 - To run the unittests, first CD into the Capstone folder and run the following command:
 ```bash
CREATE DATABASE capstone_test;
psql -d capstone_test -U postgres -a -f capstone.psql
python -m unittest test_app
```
 















   