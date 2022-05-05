# Hotel Booking RESTful APIs document

## Overview
This service provided the connection authorization to allow user to autorize and booking room in the hotel.

# Authorization
We use API keys to authenticate the request
## Common properties
> In authorization we use the our end point is `POST api/auth/...`

|body|type|
|---|---|
|username| `String`|
|password| `String`|
## Resigter

```py
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