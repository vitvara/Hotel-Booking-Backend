
# Common specification
* [Rate limits](common_specification.md?id=rate-limits)
* [Status codes](common_specification.md?id=status-codes)
* [Error responses](common_specification.md?id=error-responses)

## Rate limits
The hotel API applies the rate limits for each API endpoint

|When submit requests exceeding the rate limit|
|----------------|
|If you send requests exceeding the rate limit,you will receive an error message saying `429 Too Many Request`|

|Endpoint| Rate limit|
|---------|-----------|
|[Login](RESTful.md?id=login)|15 requests per hour|
|[Register](RESTful.md?id=register)|
||
|[Get all room](room.md?id=get-all-room)| 200 requests per minute|
|[Get all avaliable room](room.md?id=get-all-avaliable-room)
|[Get room by user](room.md?id=get-room-by-user)
||
|[Booking Room](booking_service.md?id=booking-room)|40 request per minutes|
|[Confirm Room](booking_service.md?id=confirmation)
|[Cancel Room](bookint_service.md?id=cancellation)

### Scope of rate limits
In all API that not required the authentication check rate limits from IP address but other API that required authentication we apply rate limit without distinction, even if you use the endpoint from a different IP address.

## Status codes
|Status code|Description|
|-----|-----|
|200 OK| Request successful|
|400 Bad Request| Problem with request|
|401 Unauthorized| Token is invalid or token is not specified|
|403 Forbidden| Not authorized to access the resourse|
|429 Too Many Requests| Exceeded the rate limit for requests|
|500 Server Error| Internal server error.|

## Error responses
We return the JSON data in the response body when an error occurs

__message__ `String`
Message containing information about the error

_Example error_
```json
{
    message: "Username is taken" 
}
```