import re
from Point import Point

class Car(object):
    """A new class Car, python realization"""

    __slots__ = ('__fuel_amount', '__fuel_capacity', '__fuel_consumption', '__model', '__location')

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

    def _validate_str(self, new_str):
        try:
            if not isinstance(new_str, (str)):
                raise TypeError
        except Exception as e:
            print('Incorrect string')
            raise e
            
        return re.sub("[^A-Za-z]", "", new_str)
    
    def __init__(self, fuel_capacity=60, fuel_consumption=0.6, location=Point(0,0), model='Audi', ):
        self.__fuel_amount = 0
        self.__fuel_capacity = self._validate_attr(fuel_capacity)
        self.__fuel_consumption = self._validate_attr(fuel_consumption)
        self.__location = location
        self.__model = self._validate_str(model)

    def __get_fuel_amount(self):
        return self.__amount

    def __get_fuel_capacity(self):
        return self.__capacity

    def __get_fuel_consumption(self):
        return self.__fuel_consumption

    def __get_location(self):
        return self.__location

    fuel_amount = property(__get_fuel_amount)
    fuel_capacity = property(__get_fuel_capacity)
    fuel_consumption = property(__get_fuel_consumption)
    location = property(__get_location)

    def drive_up_to_point(self, destination):
        self.__fuel_amount += destination.distance(self.__location) * self.__fuel_consumption

        try:
            if self.__fuel_amount > self.__fuel_capacity:
                raise ArithmeticError
        except Exception as e:
            print('Out of fuel!')
            raise e

        self.__fuel_capacity -= self.__fuel_amount;
        self.__location = destination

    def drive_up_to_coordinates(self, x, y):
        destination = Point(self._validate_attr(x), self._validate_attr(y))
        
        self.__fuel_amount += destination.distance(self.__location) * self.__fuel_consumption
        
        try:
            if self.__fuel_amount > self.__fuel_capacity:
                raise ArithmeticError
        except Exception as e:
            print('Out of fuel!')
            raise e
        
        self.__fuel_capacity -= self.__fuel_amount
        self.__location = destination

    def refill(self, fuel):
        try:
            if self._validate_attr(fuel) > self.__fuel_amount:
                raise ValueError
        except Exception as e:
            print('To much fuel!')
            raise e
        
        self.__fuel_capacity += self._validate_attr(fuel)
    
    def __str__(self):
        return f'Model - {self.__model}\nLocation\t{self.__location}\nFuel Amount\t {self.__fuel_amount}\nFuel Capacity\t {self.__fuel_capacity}\nFuel Consumption {self.__fuel_consumption}'

if __name__ == '__main__':
    car1 = Car()
    car2 = Car(12, 0.7, Point(4, 2), 'Volkswagen')

    print(car1, '\n')
    print(car2, '\n')

    car1.drive_up_to_point(Point(2, 4))
    car2.drive_up_to_coordinates(8, 13)

    print(car1, '\n')
    print(car2, '\n')

    car2.refill('8.19328')

    print(car2)