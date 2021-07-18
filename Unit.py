import re

class Unit(object):
    """A new class Unit, python realization"""

    __slots__ = ('__damage', '__hit_points', '__hit_points_limit', '__name')

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

    def __init__(self, name, hp, dmg):
        self.__name = self._validate_str(name)
        self.__hit_points = self._validate_attr(hp)
        self.__hit_points_limit = self._validate_attr(hp)
        self.__damage = self._validate_attr(dmg)

    def __get_name(self):
        return self.__name

    def __get_hit_points(self):
        return self.__get_hit_points

    def __get_hit_points_limit(self):
        return self.__hit_points_limit\

    def __get_damage(self):
        return self.__damage

    name = property(__get_name)
    hit_points = property(__get_hit_points)
    hit_points_limit = property(__get_hit_points_limit)
    damage = property(__get_damage)

    def ensure_is_live(self):
        try:
            if self.__hit_points == 0:
                raise ValueError
        except Exception as e:
            print('Unit Is Dead')
            raise e

    def add_hit_points(self, hp):
        self.ensure_is_live()

        if self._validate_attr(hp) <= (self.__hit_points_limit - self.__hit_points):
            self.__hit_points += self._validate_attr(hp)

    def take_damage(self, dmg):
        self.ensure_is_live()

        self.__hit_points -= self._validate_attr(dmg)

        if self.__hit_points < 0:
            self.__hit_points = 0

    def attack(self, enemy):
        enemy.ensure_is_live()
        enemy.take_damage(self.__damage)
        enemy.counter_attack(self)

    def counter_attack(self, enemy):
        enemy.ensure_is_live()
        enemy.take_damage(int(self.__damage/2))

    def __str__(self):
        return f'Name\t\t {self.__name}\nDamage\t\t {self.__damage}\nHit points\t {self.__hit_points}\nHit points limit {self.__hit_points_limit}'


if __name__ == '__main__':
    unit1 = Unit('Barbarian', 200, 30)
    unit2 = Unit("Knight", 100, 40)

    print(unit1)
    print('\n')
    print(unit2)
    print('\n')

    unit1.attack(unit2)

    print(unit1)
    print('\n')
    print(unit2)
    print('\n')