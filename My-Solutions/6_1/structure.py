from typing import Any


class Structure():
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise ValueError(f"Expected {len(self._fields)} arguments, but got {len(args)}")
        for field, arg in zip(self._fields, args):
            setattr(self, field, arg)
    
    def __repr__(self):
        values = [getattr(self, field) for field in self._fields]
        return f"{type(self).__name__}({', '.join(str(value) for value in values)})"
    
    def __setattr__(self, name, value):
        if name in self._fields or name[0] == "_":
            super.__setattr__(self, name, value)
        else:
            raise AttributeError(f"No attribute '{name}'")
        
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year', 'month', 'day')