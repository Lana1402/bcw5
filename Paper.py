class Paper(object):
    """A new class Paper, python realization"""
    
    __slots__ = ('__max_symbols', '__symbols', '__content')
    
    def _validate_attr(self, value):
        try:
            if not isinstance(value, (int, str)):
                raise TypeError
            
            if isinstance(value, str):
                value = int(value)
        except Exception as e:
            print('Incorrect value')
            raise e
        
        return value
    
    def _validate_str(self, new_str):
        try:
            if not isinstance(new_str, (str)):
                raise TypeError
        except Exception as e:
            print('Incorrect string')
            raise e
            
        return new_str
    
    def __init__(self, max_symbols=4096):
        self.__max_symbols = self._validate_attr(max_symbols)
        self.__symbols = 0
        self.__content = str()
    
    def __get_max_symbols(self):
        return self.__max_symbols
    
    def __get_symbols(self):
        return self.__symbols
    
    max_symbols = property(__get_max_symbols)
    symbols = property(__get_symbols)
    
    def add_content(self, message):
        try:
            if self.__symbols == self.__max_symbols:
                raise ArithmeticError
        except Exception as e:
            print('Out of space')
            raise e
        
        self._validate_str(message)
        
        self.__content += message[:self.__max_symbols-self.__symbols]
        self.__symbols = len(self.__content)
    
    def show(self):
        print(self.__content)
        