# Room Booking Service

## Booking Room
This API required token to authorize the token come from [login](RESTful.md?id=Login)
```
headers = {
  "headers" {
    ...,
    "Authorization": <token>
  }
}
response = request.post("http://some.hotel.url/api/hotel/book/room/<room_id>", headers=headers)
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
response = request.post("http://some.hotel.url/api/hotel/confirm/room/<room_id>", headers=headers)
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
response = request.post("http://some.hotel.url/api/hotel/cancel/room/<room_id>", headers=headers)
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
