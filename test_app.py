import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import setup_db, Actor, Movie




class AgencyTestCase(unittest.TestCase):
    """This class represents the test case"""
 
    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', '9520099', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

     

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()



        self.actor = {
            "name" : "my new actor added",
            "age" : "37",
            "gender" : "Female"
        }


        self.movie = {
            "title" : "new movie added",
            "release" : "2020"    
        }


        self.producer_token = os.environ.get('PRODUCER_TOKEN')
        self.director_token = os.environ.get('DIRECTOR_TOKEN')
        self.assistant_token = os.environ.get('ASSISTANT_TOKEN')




    def tearDown(self):
        """Executed after reach test"""
        pass


    
    

    # Test for return actors
    def test_get_actors(self):
    
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['actors'])
        self.assertEqual(data['success'], True)


   

    # Test for return movies
    def test_get_movies(self):
    
        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['movies'])
        self.assertEqual(data['success'], True) 




    # ---------------------------------------------------------
    # Director Role
    # ---------------------------------------------------------

    # Test for post new actor 
    def test_01_add_actor(self):

        response = self.client().post("/actors", json=self.actor, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 200)


        # Test for unsuccessful post empty actor 
    def test_02_uncreated_actor(self):
        request_data = {
            'name': '',
            'age': '',
        }
         
        response = self.client().post("/actors", json=request_data, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


   
    # Test for patch actor 
    def test_03_edit_actor_by_ID(self):

        edited_actor = {
           'name': 'edited name'
        }

        response = self.client().patch('/actors/1', json=edited_actor, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

  


  

    # Test for delete actor 
    def test_04_delete_actor_by_ID(self):
        new_actor = Actor(
            name='one for delete',
            age='40',
            gender='female'
        )

        new_actor.insert()
        response = self.client().delete('/actors/{}'.format(new_actor.id), headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    # Test for delete an actor does not exist
    def test_05_delete_actor(self):
        response = self.client().delete('/actors/1000', headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    # Test for post new movie 
    def test_06_add_movie(self):

        response = self.client().post("/movies", json=self.movie, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')




    
    # Test for patch movie 
    def test_07_edit_movie_by_ID(self):

        edited_movie = {
           'title': 'edited title'
        }

        response = self.client().patch('/movies/1', json=edited_movie, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    




 
    # Test for delete movie 
    def test_08_delete_movie_by_ID(self):
        new_movie = Movie(
            title='one for delete',
            release='2020'
        )

        new_movie.insert()
        response = self.client().delete('/movies/{}'.format(new_movie.id), headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')




    # ---------------------------------------------------------
    # Prdoucer Role
    # ---------------------------------------------------------


    
    # Test for post new actor 
    def test_09_add_actor(self):

        response = self.client().post("/actors", json=self.actor, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 200)

    

    # Test for unsuccessful post empty actor 
    def test_010_uncreated_actor(self):
        new_request_data = {
            'name': '',
            'age': '',
            'gender': ''
        }
         
        response = self.client().post("/actors", json=new_request_data, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


    # Test for patch actor 
    def test_011_edit_actor_by_ID(self):

        new_edited_actor = {
           'name': 'new edited name'
        }

        response = self.client().patch('/actors/1', json=new_edited_actor, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    



    # Test for delete actor 
    def test_012_delete_actor_by_ID(self):
        new_actor = Actor(
            name='one for delete',
            age='40',
            gender='female'
        )

        new_actor.insert()
        response = self.client().delete('/actors/{}'.format(new_actor.id), headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    

    # Test for delete an actor does not exist
    def test_013_delete_actor(self):
        response = self.client().delete('/actors/1000', headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    


    # Test for post new movie 
    def test_014_add_movie(self):

        response = self.client().post("/movies", json=self.movie, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 200)


   


    # Test for unsuccessful post empty movie
    def test_015_uncreated_movie(self):
        request_data = {
            'title': '' ,
            'release': ''
        }
         
        response = self.client().post("/movies", json=request_data, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')  


    # Test for patch movie 
    def test_016_edit_movie_by_ID(self):

        edited_movie_3 = {
           'release': '2021'
        }

        response = self.client().patch('/movies/1', json=edited_movie_3, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    


    # Test for delete movie 
    def test_016_delete_movie_by_ID(self):
        new_movie = Movie(
            title='one for delete',
            release='2020'
        )

        new_movie.insert()
        response = self.client().delete('/movies/{}'.format(new_movie.id), headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True) 


    

    # Test for delete a movie does not exist
    def test_017_delete_movie(self):
        response = self.client().delete('/movies/1000', headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    



    # ---------------------------------------------------------
    # Assistant Role
    # ---------------------------------------------------------

    # Test for unauthorized post new actor 
    def test_018_add_actor(self):

        response = self.client().post("/actors", json=self.actor, headers={"Authorization":"Bearer {}".format(self.assistant_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')

    


    # Test for unauthorized patch movie 
    def test_019_edit_movie_by_ID(self):

        edited_movie = {
           'title': 'edited title'
        }

        response = self.client().patch('/movies/1', json=edited_movie, headers={"Authorization":"Bearer {}".format(self.assistant_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')

    
    

     
     





  


   

    



    


    






     


    




    
    




    
