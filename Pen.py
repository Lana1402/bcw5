from Paper import Paper

class Pen(object):
    """A new class Pen, python realization"""
    
    __slots__ = ('__inkAmount', '__inkCapacity')
    
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
    
    def __init__(self, inkCapacity=4096):
        self.__inkCapacity = self._validate_attr(inkCapacity)
        self.__inkAmount = self._validate_attr(inkCapacity)
    
    def __get_ink_capacity(self):
        return self.__inkCapacity
    
    def __get_ink_amount(self):
        return self.__inkAmount
    
    inkCapacity = property(__get_ink_capacity)
    inkAmount = property(__get_ink_amount)
    
    def write(self, message, paper):
        try:
            if self.__inkAmount == 0:
                raise ArithmeticError
        except Exception as e:
            print('Out of ink')
            raise e
        
        self._validate_str(message)
        
        paper.add_content(message[:self.__inkAmount])
        
        len_sub_str = paper.max_symbols - (paper.max_symbols-paper.symbols)
        
        if len_sub_str > len(message):
            self.__inkAmount -= len(message)
        else:
            self.__inkAmount -= len_sub_str
        
        if self.__inkAmount < 0:
            self.__inkAmount = 0
    
    def refill(self):
        self.__inkAmount = self.__inkCapacity


if __name__ == '__main__':
    pen = Pen()
    paper = Paper(10)

    pen.write('Hello, world!!!', paper)

    paper.show()

    print('Pen', pen.inkAmount)
    print('Paper', paper.symbols)