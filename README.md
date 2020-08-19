# Casting Agency

## Introduction
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 


- Models:
   - Actor with attributes name, age and gender
   - Movie with attributes title and release date
- Endpoints:
   - GET /actors and /movies
   - DELETE /actors/ and /movies/
   - POST /actors and /movies and
   - PATCH /actors/ and /movies/
- Roles:
   - Casting Assistant
      - Can view actors and movies
   - Casting Director
      - All permissions a Casting Assistant has and…
      - Add or delete an actor from the database
      - Modify actors or movies
   - Executive Producer
      - All permissions a Casting Director has and…
      - Add or delete a movie from the database
- Tests:
   - One test for success behavior of each endpoint
   - One test for error behavior of each endpoint
   - At least two tests of RBAC for each role



## Running the server

From within the `Capstone` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --reload
```


### Unittesting
 - To run the unittests, first CD into the Capstone folder and run the following command:
 `CRETE DATABASE capstone_test;`
 `psql -d capstone_test -U postgres -a -f capstone.psql`
 `python -m unittest test_app`


## Running the API 
API endpoints can be accessed via https://fsndheroku-agency.herokuapp.com/


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

















   