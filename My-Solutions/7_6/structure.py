# structure.py

import sys
import inspect
from validate import Validator, validated
from validate import Validator
from collections import ChainMap

def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls

def validate_attributes(cls):
    validators = []
    types = []
    # Get the list of methods in the class
    methods = [getattr(cls, method_name) for method_name in dir(cls) if callable(getattr(cls, method_name))]

    # Filter methods with annotations
    annotated_methods = [method for method in methods if hasattr(method, "__annotations__") and len(method.__annotations__) > 0]

    for method in annotated_methods:
        setattr(cls, method.__name__, validated(method))

    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
            types.append(val.expected_type)
    cls._fields = [val.name for val in validators]
    cls._types = [type for type in types]
    cls.create_init()
    return cls

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        print("meta: ", meta)
        print("clsname: ", clsname)
        print("bases: ", bases)
        print(ChainMap({}, Validator.validators))
        return ChainMap({}, Validator.validators)
        
    @staticmethod
    def __new__(meta, name, bases, methods):
        # print("methods: ", methods)
        print("methods.maps: ", methods.maps[0])
        methods = methods.maps[0]

        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
    _fields = ()
    _types = ()

    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        locs = { }
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        exec(code, locs)
        cls.__init__ = locs['__init__']
    
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))