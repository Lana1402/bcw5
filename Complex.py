import math

class Complex(object): 
    """A new class Complex, python realization"""
    
    __slots__ = ('__real', '__imaginary')
    
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
    
    def __init__(self, real=0, imaginary=0):
        self.__real = self._validate_attr(real)
        self.__imaginary = self._validate_attr(imaginary)
    
    def __get_real(self):
        return self.__real
    
    def __get_imaginary(self):
        return self.__imaginary
    
    def __set_real(self, value):
        self.__real = self._validate_attr(value)
    
    def __set_imaginary(self, value):
        self.__imaginary = self._validate_attr(value)
    
    real = property(__get_real, __set_real)
    imaginary = property(__get_imaginary, __set_imaginary)
    
    def __iadd__(self, other):
        self.__real += other.real
        self.__imaginary += other.imaginary
        return self
    
    def __isub__(self, other):
        self.__real -= other.real
        self.__imaginary -= other.imaginary
        return self
    
    def __add__(self, other):
        return Complex(self.__real + other.real, self.__imaginary + other.imaginary)
    
    def __sub__(self, other):
        return Complex(self.__real - other.real, self.__imaginary - other.imaginary)
    
    def __imul__(self, other):
        return Complex(self.__real * other.real, self.__imaginary * other.imaginary)
    
    def __eq__(self, other):
            return self is other
    
    def __ne__(self, other):
            return self is not oth
    
    def __str__(self):
        return f'({self.__real}+{self.__imaginary}i)'
    

if __name__ == '__main__':
    p = Complex(2, '5.1')
    q = Complex(3, 7)

    print(p)

    d = p.__imul__(q)

    p.__iadd__(q)

    print(p)
    print(d)
