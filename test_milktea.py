'''
File: test_milktea.py
Description: This is the test module for the milktea class.
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

import pytest
from milktea import MilkTea
from topping import Topping

@pytest.fixture
def milk_tea():
    return MilkTea("Classic Milk Tea", "Medium", "Less", "Half", "Black", [])

# testing calculate price function for milktea
def test_calculate_price(milk_tea):
    milk_tea.toppings.append(Topping("Custard", {"TOPPINGS": {"Custard": 1.0}}))
    price = milk_tea.calculate_price()
    assert price == 6.64
