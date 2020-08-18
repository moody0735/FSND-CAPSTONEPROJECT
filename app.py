import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.models import setup_db, Actor, Movie
from auth.auth import AuthError, requires_auth


  
def create_app(test_config=None):
  # Create and configure the app
  app = Flask(__name__)
  setup_db(app)
  # Set up CORS. Allow '*' for origins
  CORS(app, resources={r"/api/*": {"origins": "*"}})





  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

    

  # Handle GET requests for list of actors.
  @app.route('/actors', methods=['GET'])
  def get_actors():
    actors = Actor.query.all()

    return jsonify({
      'success': True,
      'actors': [actor.long() for actor in actors]
    }), 200






  # Handle POST request for add a new actor.
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def add_new_actor(payload):
    body = request.get_json()
    if body.get('name') is None or body.get('age') is None or body.get('gender') is None:
      abort(422)
    
    add_name = body.get('name')
    add_age = body.get('age')
    add_gender = body.get('gender')

    try:
      new_actor = Actor(name=add_name, age=add_age, gender=add_gender)
      new_actor.insert()
      response = {
        'success': True,
        'status_code': 200,
        'create': new_actor.id
      }
      return jsonify(response)
    except Exception:
      abort(422)
    
    

  # Handle PATCH request for update an actor.
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actor')
  def update_actor(payload, actor_id):
    error = False
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

    if not actor:
      abort(404, {'message': 'Actor with id {} not found in database.'.format(actor_id)})

    try:
      data = request.json
      if "name" in data:
        actor.name = data["name"]
      if "age" in data:
        actor.age = data["age"]
      if "gender" in data:
        actor.gender = data["gender"]
      actor.update()
      actor = actor.long()
      response = {
        'success': True,
        'status_code': 200
      }
      return jsonify(response)
    except Exception:
      abort(422)
   



  # DELETE endpoint to delete actors in the database.
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actors(payload, actor_id):
    if not actor_id:
      abort(422, {'message': 'Please provide valid actor id'})

    actor_to_delete = Actor.query.filter(Actor.id == actor_id).one_or_none()

    if not actor_to_delete:
      abort(404, {'message': 'Actor with id {} not found in database.'.format(actor_id)})
       
    actor_to_delete.delete()
      
    return jsonify({
      'success': True,
      'delete': actor_id
    })


        
   

  # Handle GET requests for list of movies.
  @app.route('/movies', methods=['GET'])
  def get_movies():
    movies = Movie.query.all()

    return jsonify({
      'success': True,
      'movies': [movie.short_movie() for movie in movies]
    }), 200



  # Handle POST request for add a new movie.
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def add_movie(payload):

    body = request.get_json()
    if body.get('title') is None or body.get('release') is None:
      abort(422)

    add_title = body.get('title')
    add_release = body.get('release')

    try:
      new_movie = Movie(title=add_title, release=add_release)
      new_movie.insert()
      response = {
        'success': True,
        'status_code': 200, 
        'create': new_movie.id
      }
      return jsonify(response)
    except Exception:
      abort(422)
    


  # Handle PATCH request for update a movie.
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movie')
  def update_movie(payload, movie_id):
    error = False
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

    if not movie:
      abort(404)

    try:
      data = request.json
      if "title" in data:
        movie.title = data["title"]
      if "release" in data:
        movie.release = data["release"]
      movie.update()
      response = {
        'success': True,
        'status_code': 200
      }
      return jsonify(response)
    except Exception:
      abort(422)
    

  # DELETE endpoint to delete movies in the database.
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movie(payload, movie_id):
    if not movie_id:
      abort(422, {'message': 'Please provide valid movie id'})

    movie_to_delete = Movie.query.filter(Movie.id == movie_id).one_or_none()

    if not movie_to_delete:
      abort(404, {'message': 'Movie with id {} not found in database.'.format(movie_id)})
       
    movie_to_delete.delete()
      
    return jsonify({
      'success': True,
      'delete': movie_id
    })




  # ---------------------------------------------------------
  # Error Handling
  # ---------------------------------------------------------


  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
    }), 422




  @app.errorhandler(401)
  def unauthorized(error):
    return jsonify({
      "success": False,
      "error": 401,
      "message": 'Unathorized'
    }), 401


  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
    }), 404



  @app.errorhandler(AuthError)
  def auth_error(error):
    return jsonify({
      "success": False,
      "error": error.status_code,
      "message": error.error['description']
    }), error.status_code


  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)

