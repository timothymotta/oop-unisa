'''
File: test_topping.py
Description: This is the test module that tests the topppings.
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

import pytest
from topping import Topping

# testing topping prices
def test_topping_initialization():
    store_prices = {"TOPPINGS": {"Custard": 1.0}}
    topping = Topping("Custard", store_prices)
    assert topping.name == "Custard"
    assert topping.price == 1.0

# testing topping if price isnt found
def test_topping_price_not_found():
    store_prices = {"TOPPINGS": {}}
    topping = Topping("Unknown", store_prices)
    assert topping.name == "Unknown"
    assert topping.price == 0.0
