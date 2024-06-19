'''
File: fruittea.py
Description: This is the fruittea module which is a child class of the bubbletea class.
Author: Timothy Motta
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''
from bubbletea import BubbleTea

class FruitTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, type_of_fruit):
        super().__init__(name, size, level_of_ice, level_of_sugar, green_or_black_tea, type_of_fruit)

    # calculating the price of fruit tea based on the size and topping choices
    def calculate_price(self):
        price = self.base_tea_price
        if self.size == "Medium":
            price = price + 0.85
        elif self.size == "Large":
            price = price + 1.2
        elif self.size == "Small":
            price = price + 0
        for topping in self.toppings:
            price = price + topping.price
        return price