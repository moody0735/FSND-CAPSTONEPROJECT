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



        self.producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9mTlJma0gtcUpvRUMwUktjb0tLUyJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwNTAzMGRhMWY2MDMwMDE5YjA4ZTNhIiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTk3ODAwODQ0LCJleHAiOjE1OTc4MDgwNDQsImF6cCI6ImsydWMzbGFXejNhejMxd3p1eEVuU1RQb1VuNnhFVzFqIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.t5rqvVUSBq6NKc0NaDA8o8p_vLLB6xHf8vdyS8WvDHYuWMkvZoF0JX8LLRSul9GsMTeTdWqZEwKXQCirnUWDldWtF7TDAf85DmB5VE-WdCOCOgMpoB7WqS45f2x9jU2qBx8tPRXK7rmacSXtJLrWsAInOJYcAHTN_wTSXGAXye0XHQputO494_-1U5yJVLn5q_3j2ygEAi2bqKtW0cJ19EogWUa20oaQUYM_nD27gqXcWRnqN558MEvRSuwB2bEUSziVLPSu3mSMC187ixdDf2KQHyWr2OoA-wmQIlQ7RFnE_5RJjnIKpCVbfbM_z9kR2LNv9hYW861MVQrsf_sqVg&expires_in=7200"
        self.director_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9mTlJma0gtcUpvRUMwUktjb0tLUyJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwNTA1Y2RhMTViN2IwMDEzNjFlZTk4IiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTk3ODAwOTYyLCJleHAiOjE1OTc4MDgxNjIsImF6cCI6ImsydWMzbGFXejNhejMxd3p1eEVuU1RQb1VuNnhFVzFqIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9ycyJdfQ.oehKUMxB9bcSKrCRL46lMSgzKQmPt4uJ0SEBY71Kt_7j5hQ1RnBfJtlroAyfs6an7BPNmZGLHoioNs_OaiCFLLw3322SHhxf-3BUcu-2SlOuwGQw2JxRrTpf18kHX1vORicdECi7MZSXIXs_n0kHZPSZxaOM23R7h7GsbQBFDMaQPamflWCcen_eTk5Ow02erHPn7plsFpkTLwIFE-jnWaMkfG1LmanJ4SO6ROizPUhz7Fgm51oPpKs8qHRyLIdLG9EgdCTQkF4JN1qbWL39b-3E_aBRauj_-PnndkwXutlOc_skePkCnCJycbV0Sybo-VVXpFDn20DAQ6GL0YhXuw"
        self.assistant_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9mTlJma0gtcUpvRUMwUktjb0tLUyJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzMzM2NzMzYWNkMGUwMDNhMWEwYzExIiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTk3ODAxMDUxLCJleHAiOjE1OTc4MDgyNTEsImF6cCI6ImsydWMzbGFXejNhejMxd3p1eEVuU1RQb1VuNnhFVzFqIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.TGEmYB9hwRdGC-DaqJAzwPiDsIlRenzOU7XJ7L6DhTkDElIWnyIGxMHXEtVhpUFcHpr3gmUXyNFkcT4D8UOzCrJBUy5X76ed7uTt0V7gIFqY3SjhSnXWt8K8zcSL_ZkF77GeIDK5bOYWzS7HtOPlarS56CfPxrwbhS5nhM8wY2Yo5VqyE7W2L1Tmlw-cJgd1NNbZvcNKJkv9keC9frEHcR8iXldd_hFU_kt5eKtLzCI-UmjOjoiHzX9xbfLsYNfR1QaWafq_ChJ-vLZRoSvCBifpZjswZzQ1NhwjBv-IF7OZZUIXqAE5Cdz8QD77CYmL1OVpj-Z7U4Rnqfw72ffXQQ"



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

    






  


   

    



    


    






     


    




    
    




    
