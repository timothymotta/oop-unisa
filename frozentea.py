'''
File: frozentea.py
Description: This is the frozentea module which is a child class of the bubbletea class.
Author: Timothy Motta
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''
from bubbletea import BubbleTea

class FrozenTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings):
        super().__init__(name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings)

    def calculate_price(self):
        price = self.base_tea_price + 3.0
        if self.size == "Medium":
            price = price + 0.85
        elif self.size == "Large":
            price = price + 1.2
        elif self.size == "Small":
            price = price + 0
        for topping in self.toppings:
            price = price + topping.price
        return price