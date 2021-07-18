import re

class Gun(object):
    """A new class Gun, python realization"""

    __slots__ = ('__amount', '__capacity', '__isReady', '__model', '__totalShots')

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
            
        return re.sub("[^A-Za-z]", "", new_str)

    def __init__(self, model='Beretta', capacity=8):
        self.__model = self._validate_str(model);
        self.__amount = 0;
        self.__capacity = self._validate_attr(capacity);
        self.__totalShots = 0;
        self.__isReady = False;

    def __get_amount(self):
        return self.__amount

    def __get_capacity(self):
        return self.__capacity

    amount = property(__get_amount)
    capacity = property(__get_capacity)

    def ready(self):
        return self.__isReady

    def prepare(self):
        self.__isReady = True

    def reload(self):
        self.__amount = self.__capacity

    def shoot(self):
        try:
            if not self.ready():
                raise ValueError('Not ready!!!')

            if (self.__amount == int(0)):
                raise ValueError('Out of rounds')
        except Exception as e:
            raise e

        print('Bang!')
            
        self.__amount -= 1
        self.__totalShots += 1

    def __str__(self):
        return f'Model - {self.__model}\nCapacity\t{self.__capacity}\nAmount\t\t{self.__amount}\nTotal shots\t{self.__totalShots}'


if __name__ == '__main__':
    gun = Gun('Revo,lve5r', 6)
    gun1 = Gun()

    print(gun)
    # print(gun1)

    gun.prepare()
    gun.reload()

    print(gun)

    i = 0

    while i < gun.amount:
        gun.shoot()
        # i += 1

    print(gun)