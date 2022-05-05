# Room Booking Service
## Common properties
> The End point for this API is `POST /api/hotel/room/...`  

|headers| type |description|
|---|---|--|
|token| `String`| token used to authorize when user want book room or get room that user has been reserved |

|bodys|type|description|
|---|---|---|
|`timestamp`|`datetime`| The time that client has created the request|
|`room_id`|`int`| Room id selected from user|

## Booking Room
This API required token to authorize the token come from [login](RESTful.md?id=Login)
```py
headers = {
  "headers" {
    ...,
    "Authorization": <token>
  }
}

body = {
  "timestamp": <time>,
  "room_id": <room_id>
}

response = request.post("http://some.hotel.url/api/hotel/room/book/", headers=headers, data=body)
```

Success case
```js
status_code: 202
message: "Successfully booking room for <username> <user_id>"
```

failed case

Room already reserved.
```js
status_code: 200
message: "This room has already been reserved.
```

Not login
```js
status_code: 402
message: "Please Login before booking room"
```
## Confirmation
The customer must pay for the accommodation in advance so they can confirm the booking.
```py
# token: string
headers = {
  "headers" {
    ...,
    "Authorization": <token>
  }
}

body = {
  "timestamp": <time>,
  "room_id": <room_id>
}

response = request.post("http://some.hotel.url/api/hotel/room/confirm", headers=headers, data=body)
```

success case
```
status_code: 200
message: "Room <room_id> has been confirmed."
```

failed case

Customer haven't reserved a room yet.
```
status_code: 400
message: "You have not reserved a room yet."
```
Customer haven't pay for accommodation yet.
```
status_code: 400
message: "You have not pay for accommodation yet."
```
## Cancellation
```py
# token: string
headers = {
  "headers" {
    ...,
    "Authorization": <token>
  }
}

body = {
  "timestamp": <time>,
  "room_id": <room_id>
}

response = request.post("http://some.hotel.url/api/hotel/room/cancel", headers=headers, data=body)
```

success case
```
status_code: 200
message: "Room <room_id> has been cancel."
```

failed case
```
status_code: 400
message: "You have not reserved a room yet."
```
