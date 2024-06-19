'''
File: test_store.py
Description: This is the test module for the store class.
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

import pytest
from store import Store
from fruittea import FruitTea
from milktea import MilkTea
from sparklingtea import SparklingTea
from hottea import HotTea
from frozentea import FrozenTea
from topping import Topping

@pytest.fixture
def store():
    return Store()

# testing order tea function
def test_order_tea(store):
    topping = Topping("Custard", store.prices)
    tea = store.order_tea(FruitTea, "Tropical Fruit Tea", "Large", "Regular", "Full", "Green", [topping])
    assert tea.name == "Tropical Fruit Tea"
    assert store.earnings == tea.calculate_price()
    assert len(store.orders) == 1

# testing the order history
def test_view_order_history(store, capsys):
    topping = Topping("Custard", store.prices)
    store.order_tea(FruitTea, "Tropical Fruit Tea", "Large", "Regular", "Full", "Green", [topping])
    store.view_order_history()
    captured = capsys.readouterr()
    assert "Tropical Fruit Tea" in captured.out

# testing string converter
def test_store_str(store):
    assert str(store) == "TOTAL EARNINGS: \n$0.00, \n\nTOTAL ORDERS: \n0\n"
