from typing import get_type_hints

class TypeData:
    def __init__(self, data: dict):
        """
        ## TypeData
        
        Define types for given data. Makes autocompletion easier and api handling so much more pleasant.
        
        Give it a try like this:
        ```
        data = {"name": "Sarah", "age": 21}
        
        class MyData(TypeData):
            name: str
            age: int
            
        typeddata = MyData(data)
        
        print(typeddata.name)
        ```
        
        :param data: Data
        :type data: `dict`
        """
        types = get_type_hints(self.__class__)
        self.__data__ = {}
        
        for key, value in data.items():
            self.__data__[key] = value
            
            if isinstance(value, dict):
                if issubclass(types[key], TypeData):
                    value = TypeData(value)
            
            setattr(self, key, value)
            
        # Adding missing data as None
        for key, value in types.items():
            if not key in data.keys():
                setattr(self, key, None)

    def __getattr__(self, name):
        raise NameError(f"name {name} is not defined")
            
    def __getitem__(self, item):
        if hasattr(self, item):
            value = getattr(self, item)
            if isinstance(value, TypeData):
                return value
            return value
        
    def __str__(self):
        return f'{self.__data__}'
        
    def __iter__(self):
        return iter(self.__data__)
        
    def __repr__(self):
        return f'TypeData({self.__data__})'
