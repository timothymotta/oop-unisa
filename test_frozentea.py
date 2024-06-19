'''
File: test_frozentea.py
Description: This is the test module for the frozentea class.
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''
import pytest
from frozentea import FrozenTea
from topping import Topping

@pytest.fixture
def frozen_tea():
    return FrozenTea("Frozen Mango Tea", "Medium", "Regular", "Full", "Green", [])

def test_calculate_price(frozen_tea):
    frozen_tea.toppings.append(Topping("Mango Popping Pearls", {"TOPPINGS": {"Mango Popping Pearls": 0.4}}))
    price = frozen_tea.calculate_price()
    assert price == 8.75

