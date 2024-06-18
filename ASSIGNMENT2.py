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
        toppings_str = ', '.join([str(t) for t in self.toppings])
        return (f'{self.name} ({self.size}, {self.green_or_black_tea} tea, '
                f'Ice: {self.level_of_ice}, Sugar: {self.level_of_sugar}, '
                f'Toppings: {toppings_str})')

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

# class for fruit tea inheriting from parent class BubbleTea
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
        elif self.size == 'Small':
            price = price + 0
        for topping in self.toppings:
            price = price + topping.price
        return price

# class for milk tea inheriting from parent class BubbleTea
class MilkTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings):
        super().__init__(name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings)

    # calculating price for milk tea based on size and topping choices
    def calculate_price(self):
        price = self.base_tea_price + 0.29
        if self.size == 'Medium':
            price = price + 0.85
        elif self.size == 'Large':
            price = price + 1.2
        elif self.size == 'Small':
            price = price + 0
        for topping in self.toppings:
            price = price + topping.price 
        return price

# class for sparkling tea inheriting from parent class BubbleTea
class SparklingTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings):
        super().__init__(name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings)

    # calculating price for sparkling tea based on size and topping choices
    def calculate_price(self):
        price = self.base_tea_price + 0.19
        if self.size == 'Medium':
            price = price + 0.85
        elif self.size == 'Large':
            price = price + 1.2
        elif self.size == 'Small':
            price = price + 0
        for topping in self.toppings:
            price = price + topping.price
        return price

# class for hot tea inheriting from parent class BubbleTea
class HotTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings):
        super().__init__(name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings)

    def calculate_price(self):
        price = self.base_tea_price + 0.24
        if self.size == 'Medium':
            price = price + 0.85
        elif self.size == 'Large':
            price = price + 1.2
        elif self.size == 'Small':
            price = price + 0
        for topping in self.toppings:
            price = price + topping.price
        return price

# class for frozen tea inheriting from parent class BubbleTea
class FrozenTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings):
        super().__init__(name, size, level_of_ice, level_of_sugar, green_or_black_tea, toppings)

    def calculate_price(self):
        price = self.base_tea_price + 3.0
        if self.size == 'Medium':
            price = price + 0.85
        elif self.size == 'Large':
            price = price + 1.2
        elif self.size == 'Small':
            price = price + 0
        for topping in self.toppings:
            price = price + topping.price
        return price

# class for topping
class Topping:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    # string converter, converts name and price to string, price is 2 decimal places
    def __str__(self):
        return f'{self.name} (${self.price:.2f})'

# class for store, contains functions that order and/or create tea
class Store:
    def __init__(self):
        self.earnings = 0.0
        self.orders = []
        self.prices = {
            'BASE PRICE': 4.5,
            'SIZE OF TEA': {
                'Small': 0.0,
                'Medium': 0.85,
                'Large': 1.2,
            },
            'TYPE OF TEA': {
                'Fruity': 0.15,
                'Milky': 0.29,
                'Sparkling': 0.19,
                'Hot': 0.24,
                'Frozen': 3.0,
            },
            'FRUITS': {
                'Mango': 0.3, 'Lychee': 0.1, 'Apple': 0.2,
                'Grape': 0.4, 'Melon': 0.5, 'Grapefruit': 0.1,
                'Lemon': 0.3, 'Guava': 0.2, 'Passionfruit': 0.25,
                'Strawberry': 0.2, 'Pomegranate': 0.45, 'Peach': 0.1,
                'Tropical': 0.65, 'Watermelon': 0.35,
            },
            'FLAVOURS': {
                'Mint Choc': 0.3, 'Thai': 0.35, 'Salted Caramel': 0.2,
                'Roasted': 0.4, 'Earl Grey': 0.5, 'Vanilla': 0.1,
                'Assam': 0.3, 'Hazelnut': 0.2, 'Oolong': 0.25,
                'Jasmine': 0.2, 'Matcha': 0.45, 'Taro': 0.65,
                'Chocolate': 0.4,
            },
            'TOPPINGS': {
                'Custard': 1.0, 'Mousse': 2.4, 'Pearls': 1.2,
                'Cookie Crumb': 0.75, 'Mixed Jellies': 0.35, 'Herbal Jelly': 0.45,
                'Coconut Jelly': 0.5, 'Aloe Vera': 0.7, 'Mango Popping Pearls': 0.4,
                'Strawberry Popping Pearls': 0.4, 'Apple Popping Pearls': 0.4,
            }
        }

    # function to order tea
    def order_tea(self, tea_class, name, size, ice_level, sugar_level, tea_type, toppings):
        tea = tea_class(name, size, ice_level, sugar_level, tea_type, toppings)
        self.earnings = self.earnings + tea.calculate_price()
        self.orders.append(tea)
        return tea

    # function to store order history
    def view_order_history(self):
        for order in self.orders:
            print(order)

    # string converter 
    def __str__(self):
        return f'Total Earnings: \n${self.earnings:.2f}, \nTotal Orders: \n{len(self.orders)}\n'

def main():
    store = Store()

    mango_topping = Topping("Mango", 0.3)
    lychee_topping = Topping("Lychee", 0.1)
    strawberry_topping = Topping("Strawberry", 0.4)

    print("|=================================================================================================|\n")
    print("|                    ░█▀▀█ ░█─░█ ░█▀▀█ ░█▀▀█ ░█─── ░█▀▀▀ 　 ▀▀█▀▀ ░█▀▀▀ ─█▀▀█                     |")
    print("|                    ░█▀▀▄ ░█─░█ ░█▀▀▄ ░█▀▀▄ ░█─── ░█▀▀▀ 　 ─░█── ░█▀▀▀ ░█▄▄█                     |")
    print("|                    ░█▄▄█ ─▀▄▄▀ ░█▄▄█ ░█▄▄█ ░█▄▄█ ░█▄▄▄ 　 ─░█── ░█▄▄▄ ░█─░█                     |\n")
    print("|=================================================================================================|")

    store.order_tea(FruitTea, "Tropical Fruit Tea", "Large", "Regular", "Full", "Green", [mango_topping, lychee_topping])
    store.order_tea(MilkTea, "Classic Milk Tea", "Medium", "Less", "Half", "Black", [lychee_topping])
    store.order_tea(SparklingTea, "Sparkling Lemon Tea", "Small", "Full", "Full", "Green", [mango_topping])
    store.order_tea(HotTea, "Hot Earl Grey Tea", "Large", "None", "None", "Black", [])
    store.order_tea(FrozenTea, "Frozen Mango Tea", "Medium", "Regular", "Full", "Green", [mango_topping])
    
    store.order_tea(FruitTea, "Tropical Fruit Tea", "Large", "Regular", "Full", "Green", [mango_topping, lychee_topping])

    
    
    # display store
    print(store)
    store.view_order_history()

if __name__ == "__main__":
    main()
