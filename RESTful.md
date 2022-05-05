# Hotel Booking RESTful APIs document

## Overview
This service provided the connection authorization to allow user to autorize and booking room in the hotel.

# Authorization
We use API keys to authenticate the request

## Resigter
```py
"""
username: String
password: String
"""
body = {
    username: <username>, 
    password: <password>  
}

response = requests.post("http://some.hotel.url/api/auth/register", data=body) 
```
success response
```js
status_code: 200 
message: "Register success"
```
failed response username is taken
```js
status_code: 400
message: "Username is taken" 
```
## Login
```py
"""
username: String
password: String
"""
body = {
    username: <username>, 
    password: <password>  
}

response = requests.post("http://some.hotel.url/api/auth/login", data=body) 
```

success case
```js
status_code: 200
message: "Sucessfuly login"
token: <generated token>
```

failed case
```js
status_code: 401
message: "Invalid username and/or password"
```