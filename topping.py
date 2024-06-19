'''
File: topping.py
Description: This is the topping class which is a class that stores the name and price of a topping.
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

class Topping:
    def __init__(self, name, store_prices):
        self.__name = name
        # self.__price = price
        if name in store_prices["TOPPINGS"]:
            self.__price = store_prices["TOPPINGS"][name]
        else:
            self.__price = 0 

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    # string converter, converts name and price to string, price is 2 decimal places
    def __str__(self):
        return f"{self.name} (${self.price:.2f})"