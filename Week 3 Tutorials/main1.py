from typing import ClassVar


class Animal:
    i: ClassVar[int] = 6
    __j: ClassVar[int] = 2  # private attribute

    # def __init__(self):

    # private method
    def __my_private_func(self):
        return self.__j * self.i

    # setters + getters
    def set_j(self, param1: int) -> None:
        self.__j = param1

    # calling a private function
    def multiplier(self):
        return self.__my_private_func()


my_animal: Animal = Animal()
print(my_animal.multiplier())
my_animal.set_j(8)
print(my_animal.multiplier())

animal1 = Animal()
print(animal1.multiplier())

animal2: Animal = Animal()
print(animal2.multiplier())
animal2.set_j(3)
print(animal2.multiplier())