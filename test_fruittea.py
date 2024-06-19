'''
File: test_fruittea.py
Description: This is the test module for the fruittea class.
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

import pytest
from fruittea import FruitTea
from topping import Topping

# fixture to compare results with
@pytest.fixture
def fruit_tea():
    return FruitTea("Tropical Fruit Tea", "Large", "Regular", "Full", "Green", [])

# testing calculate price function for fruittea
def test_calculate_price(fruit_tea):
    fruit_tea.toppings.append(Topping("Mango", {"TOPPINGS": {"Mango": 0.3}}))
    price = fruit_tea.calculate_price()
    assert price == 6.0
