'''
File: test_sparklingtea.py
Description: This is the test module for the sparklingtea class.
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

import pytest
from sparklingtea import SparklingTea
from topping import Topping

@pytest.fixture
def sparkling_tea():
    return SparklingTea("Sparkling Lemon Tea", "Small", "Full", "Full", "Green", [])

def test_calculate_price(sparkling_tea):
    sparkling_tea.toppings.append(Topping("Mixed Jellies", {"TOPPINGS": {"Mixed Jellies": 0.35}}))
    price = sparkling_tea.calculate_price()
    assert price == 5.04
