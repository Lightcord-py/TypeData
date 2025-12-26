# TypeData

Define types for given data. Makes autocompletion easier and api handling so much more pleasant.

Give it a try like this:
```py
data = {"name": "Sarah", "age": 21}

class MyData(TypeData):
    name: str
    age: int
    
typeddata = MyData(data)

print(typeddata.name)
```