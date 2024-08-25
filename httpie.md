# Get
```
http GET http://127.0.0.1:8000/mymodel
```

# Post

## With invalid choice
```
http POST http://127.0.0.1:8000/mymodel/1 type='lolo' name='my_name'
```
## With valid choice
```
http POST http://127.0.0.1:8000/mymodel/1 type='cosmic' name:=null
http POST http://127.0.0.1:8000/mymodel/1 type='extra' name='abc'
http POST http://127.0.0.1:8000/mymodel/1 type='extra'
```

# Update

## With invalid choice
```
http PATCH http://127.0.0.1:8000/mymodel/1 type='down'
```

## With valid choice
```
http PATCH http://127.0.0.1:8000/mymodel/22 type='additional'
http PATCH http://127.0.0.1:8000/mymodel/26 name:=null
```
