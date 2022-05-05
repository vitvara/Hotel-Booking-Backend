# Room

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

## GET Room by user id
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



