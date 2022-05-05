# Room
## Common properties
> The End point for this API is `GET /api/hotel/...`  

|headers| type |description|
|---|---|--|
|token| `String`| token used to authorize when user want book room or get room that user has been reserved |

### Response
 The server must return the room information to the client in form of `JSON`. There are only one end point that required token is get room byuser otherwise don't required

|key|type|description|
|---|---|---|
|`id`| `int`|room unique id|
|`room_number`| `int`| room number in each building|
|`building`| `String`| building name or code|
|`floor`|`int`| build floor|
|`bed`|`int`| number of bed in this room|
|`price`|`int`| price of the room|
|`max_guest`|`int`| maximum user that this room can handle|
|`status`|`String`|Booking status. Have three status `avaliable` is user can book this room `pending` is someone is doing the payment (means if they failed to pay the accommodation another user can book this room) `reserved` is the room has already reserved
|`type`|`String`| Room type |
|`user_id`|`int`| ID or user that reserved of in process to booking the room if the room is avaliable `user_id` will be null|



## GET All room
```py
response = requests.get("http://some.hotel.url/api/hotel/get-all-room") 
```

Example data
```
[
    {
        id: <id>,
        room_number: <room number>,
        building: <building>,
        floor: <floor>,
        bed: <bed>,
        price: <price>,
        max_guest: <max guest>,
        status: <status>,
        type: <type>,
        user_id: <user_id>,
    }
    ...
]
```

## GET All avaliable room
```py
response = requests.get("http://some.hotel.url/api/hotel/get-all-avaliable-room")
```

Example data
```
[
    {
        id: <id>,
        room_number: <room number>,
        building: <building>,
        floor: <floor>,
        bed: <bed>,
        price: <price>,
        max_guest: <max guest>,
        status: "avaliable",
        type: <type>,
        user_id: <user_id>,
    }
    ...
]
```

## GET Room by user
You need to have token from login to call this method
```py
headers = {
  "headers" {
    ...,
    "Authorization": <token>
  }
}

response = requests.get("http://some.hotel.url/api/hotel/get-room", headers=headers))
```

Example data
```
[
    {
        id: <id>,
        room_number: <room number>,
        building: <building>,
        floor: <floor>,
        bed: <bed>,
        price: <price>,
        max_guest: <max guest>,
        status: "reserved",
        type: <type>,
        user_id: user-id,
    }
    ...
]
```

failed case
```
status_code: 401
message: "Authorize failed: Please login before you call this method"
```



