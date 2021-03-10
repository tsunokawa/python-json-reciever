# python-json-reciever

## Reciever

```
python json-reciever.py
```

## Test

```
curl -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d '{"user":{"first_name":"hoge","last_name":"test","email":"test@example.com","role":"admin"}}' http://127.0.0.1:1234/log
```

```
127.0.0.1 - - [08/Nov/2020 00:10:33] "POST /log HTTP/1.1" 200 -

{
  "user": {
    "first_name": "hoge",
    "last_name": "test",
    "email": "test@example.com",
    "role": "admin"
  }
}
```

