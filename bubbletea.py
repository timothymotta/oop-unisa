'''
File: bubbletea.py
Description: This is the bubbletea class which is the parent class, it's an abstract class as well. 
Author: Timothy Motta
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''
# import abstract class
from abc import ABC, abstractmethod

# class for bubble tea, using encapsulation by making the variables private
class BubbleTea(ABC):
    base_tea_price = 4.5

    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings):
        self.__name = name
        self.__size = size
        self.__level_of_ice = level_of_ice
        self.__level_of_sugar = level_of_sugar
        self.__green_or_black_tea = green_or_black_tea
        self.__toppings = toppings

    # getters
    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def level_of_ice(self):
        return self.__level_of_ice

    @property
    def level_of_sugar(self):
        return self.__level_of_sugar

    @property
    def green_or_black_tea(self):
        return self.__green_or_black_tea

    @property
    def toppings(self):
        return self.__toppings

    @abstractmethod
    def calculate_price(self):
        pass

    def __str__(self):
        toppings_str = ", ".join([str(t) for t in self.toppings])
        return (f"TEA: {self.name} ({self.size}, {self.green_or_black_tea} tea) "
                f"\nAMOUNT OF ICE: {self.level_of_ice} \nAMOUNT OF SUGAR: {self.level_of_sugar} "
                f"\nTOPPINGS: {toppings_str})\n")

    # function for adding topping
    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)
            print(f"{topping} has been added to your bubble tea! :)")
        else:
            print(f"{topping} has already been added to your bubble tea.")

    # function for removing topping
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
            print(f"{topping} has been removed from your bubble tea! :)")
        else:
            print(f"{topping} is not in your bubble tea.")