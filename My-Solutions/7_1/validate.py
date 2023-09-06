import inspect

def validated(func):
    print('Adding validator to', func.__name__)
    def wrapper(*args, **kwargs):
        bound = inspect.signature(func).bind(*args, **kwargs)
        func.__annotations__.pop('return', None)
        for name, val in func.__annotations__.items():
            val.check(bound.arguments[name])
        result = func(*args, **kwargs)
        return result
    return wrapper

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        bound = inspect.signature(self.func).bind(*args, **kwargs)
        for name, val in self.func.__annotations__.items():
            val.check(bound.arguments[name])
        result = self.func(*args, **kwargs)
        return result

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value
    
    def __set__(self, instance,	value):
        instance.__dict__[self.name] = self.check(value)
    
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass