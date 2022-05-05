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
message: "This <room_id> has been cancel."
```

failed case
```
status_code: 400
message: "You have not reserved a room yet."
```
