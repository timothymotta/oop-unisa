'''
File:
Description: This is a program made for a bubble tea store which implements the use of different Object Oriented Programming techniques. 
It also uses different classes and functions to perform different things in the program. 
Author: Timothy Motta
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy
'''


import random
# import abstract class
from abc import ABC, abstractmethod

# class for bubble tea
class BubbleTea(ABC):
    base_tea_price = 4.5
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings, price):
        self.__name = name
        self.__size = size
        self.__level_of_ice = level_of_ice
        self.__level_of_sugar = level_of_sugar
        self.__green_or_black_tea = green_or_black_tea
        self.__toppings = toppings
        self.__price = price

# getters
def get_name(self):
    return self.__name

def get_size(self):
    return self.__size

def get_level_of_ice(self):
    return self.__level_of_ice

def get_level_of_sugar(self):
    return self.__level_of_sugar

def get_green_or_black_tea(self):
    return self.__green_or_blac_tea

def get_toppings(self):
    return self.__toppings

def get_price(self):
    return self.__price

# abstract method and function for calculating tea price
@abstractmethod
def calculate_tea_price(self):
    pass

def __str__(self):
    
# function for adding topping
def add_topping(self, topping):
    pass

# function for removing topping
def remove_topping(self, topping):
    pass

# class for fruit tea inheriting from parent class BubbleTea
class FruitTea(BubbleTea):
    def __init__(self):
        def calculate_price(self):
            price = self.base_tea_price
        if self.size == "Medium":
            price = price + 0.85
        elif self.size == "Large":
            price = price + 1.2
        return price 

# class for milk tea inheriting from parent class BubbleTea
class MilkTea(BubbleTea):
    def __init__(self):
        super().__init__()
pass

# class for sparkling tea inheriting from parent class BubbleTea
class SparklngTea(BubbleTea):
    def __init__(self):
        super().__init__()
        pass
    
# class for hot tea inheriting from parent class BubbleTea
class HotTea(BubbleTea): 
    def __init__(self):
        super().__init__()
        pass

# class for frozen tea inheriting from parent class BubbleTea
class FrozenTea(BubbleTea):
    def __init__(self):
        super().__init__()
        pass

# class for topping inheriting from parent class BubbleTea
class Topping(BubbleTea):
    def __init__(self):
        super().__init__()
        pass

# class for store, contains functions that order and/or create tea
class Store:
    def __init__(self):
        # function for ordering tea
        def ordering_tea():
         pass
        
        # function for creating tea
        def creating_tea():
         pass