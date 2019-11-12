All data have json form:
json
{
    "data" : "...",
    "message" : "..."
}

User endpoint
    GET /user/{id}
    responce:
    - 200 OK
        -user exists
    - 400 Error 
        -user does not exist

    POST /user/{id}
    responce:
    - 200 OK
        -user created
    - 400 Error
        -user was not created or already exists

    PUT /user/{id}
    responce:
    - 200 OK
        -user creditals updated
    - 400 Error
        -user was not found

    DELETE /user/{id}
    responce:
    - 200 OK
        -user deleted
    - 400 Error
        -user was not found

GET /user/files
response:
- 200 OK
    authenticated