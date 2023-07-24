## API DOCUMENTATION

#### CREATE SHORT URL

This API helps you to generate a fresh shortned encoded URL for the given URL.

```
/create
```

api
```
{
 "url" : "string"
}
```

response
```
{
 "msg":
    {
      "short_url": "string"
    },
 "status_code": 201
}
```

```
{
 "msg": "String",
 "status_code": 40x/50x
}
```

--------------------------------------------------------------------------------

#### GET SHORT URL

This API helps you to fetch the shortned encoded URL for the given long URL.

```
/getShortUrl
```

api
```
{
 "url" : "string"  // the long URL
}
```

response
```
{
 "msg":
    {
      "short_url": "string",
      "msg": "string"
    },
 "status_code": "201/40x/50x"
}
```

--------------------------------------------------------------------------------

#### GET LONG URL

This API helps you to fetch the original URL for the given shortened URL.

```
/getLongUrl
```

api
```
{
 "url" : "string"  // the short URL
}
```

response

```
{
 "msg":
    {
      "short_url": "string",
      "msg": "string"
    },
 "status_code": "201/40x/50x"
}
```
--------------------------------------------------------------------------------

#### DELETE LONG URL

This API helps you to delete the original and shortened URL for the given original URL details from the DB.

```
/delete
```

api
```
{
 "url" : "string"  // the long URL
}
```

response

```
{
 "msg": "string",
 "status_code": "201/40x/50x"
}
```

--------------------------------------------------------------------------------