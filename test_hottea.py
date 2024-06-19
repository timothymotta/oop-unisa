'''
File: test_hottea.py
Description: This is the test module for the hottea class.
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

import pytest
from hottea import HotTea
from topping import Topping

@pytest.fixture
def hot_tea():
    return HotTea("Hot Earl Grey Tea", "Large", "None", "None", "Black", [])

def test_calculate_price(hot_tea):
    hot_tea.toppings.append(Topping("Mousse", {"TOPPINGS": {"Mousse": 2.4}}))
    price = hot_tea.calculate_price()
    assert price == 8.14
