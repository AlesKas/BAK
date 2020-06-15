All data have json form:
json
{
    "data" : "...",
    "message" : "..."
}

User endpoint
    GET /users
    - 200 OK
        - returns json dict of all users

    GET /users/{id}
    responce:
    - 200 OK
        -user exists
    - 400 Error 
        -user does not exist

    POST /users/{id}
    responce:
    - 200 OK
        -user created
    - 400 Error
        -user was not created or already exists

    PUT /users/{id}
    responce:
    - 200 OK
        -user creditals updated
    - 400 Error
        -user was not found

    DELETE /users/{id}
    responce:
    - 200 OK
        -user deleted
    - 400 Error
        -user was not found

GET /user/files
response:
- 200 OK
    authenticated