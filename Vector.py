import math

class Vector(object):
    """A new class Vector, python realization"""
    
    __slots__ = ('__x', '__y')
    
    def _validate_attr(self, value):
        try:
            if not isinstance(value, (int, float, str)):
                raise TypeError
            
            if isinstance(value, str):
                parts = value.split('.')
                
                if len(parts) == 1:
                    value = int(value)
                else:
                    value = float(value)
        except Exception as e:
            print('Incorrect value')
            raise e
        
        return value
    
    def __init__(self, x=0, y=0):
        self.__x = self._validate_attr(x)
        self.__y = self._validate_attr(y)
    
    def __get_x(self):
        return self.__x
    
    def __get_y(self):
        return self.__y
    
    def __set_x(self, value):
        self.__x = self._validate_attr(value)
    
    def __set_y(self, value):
        self.__y = self._validate_attr(value)
    
    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)
    
    def len(self):
        return math.hypot(self.__x, self.__y)
    
    def __iadd__(self, other):
        self.__x += other.x
        self.__y += other.y
        return self
    
    def __isub__(self, other):
        self.__x -= other.x
        self.__y -= other.y
        return self
    
    def __add__(self, other):
        return Vector(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other):
        return Vector(self.__x - other.x, self.__y - other.y)
    
    def __eq__(self, other):
            return self is other
    
    def __ne__(self, other):
            return self is not oth
    
    def __str__(self):
        return f'({self.__x}, {self.__y})'
    

if __name__ == '__main__':
    p = Vector(2, 5)
    q = Vector(3, 7)
    d = p.__add__(q)

    p.__iadd__(q)

    print(p)
    print(d)
