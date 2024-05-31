import random
from abc import ABC, abstractmethod
# class for bubble tea
class BubbleTea:
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings, price):
        self.__name = name
        self.__size = size
        self.__level_of_ice = level_of_ice
        self.__level_of_sugar = level_of_sugar
        self.__green_or_black_tea = green_or_black_tea
        self.__toppings = toppings
        self.__price = price


# class for fruit tea
class FruitTea(BubbleTea):
    def __init__(self):
        super().__init__()
pass

# class for milk tea
class MilkTea(BubbleTea):
    def __init__(self):
        super().__init__()
pass

# class for sparkling tea
class SparklngTea(BubbleTea):
    def __init__(self):
        super().__init__()
        pass
    
# class for hot tea
class HotTea(BubbleTea):
    def __init__(self):
        super().__init__()
        pass

# class for frozen tea
class FrozenTea(BubbleTea):
    def __init__(self):
        super().__init__()
        pass

# class for topping
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
