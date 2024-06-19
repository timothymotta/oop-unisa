'''
File: test_bubbletea.py
Description: This is the test module for bubbletea which tests the bubbletea class.
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''
import pytest
from bubbletea import BubbleTea

class TestBubbleTea:
    class MockBubbleTea(BubbleTea):
        def calculate_price(self):
            return 10.0
        
    # creating fixture to compare results with
    @pytest.fixture
    def bubble_tea(self):
        return self.MockBubbleTea("Test Tea", "Large", "Full", "Full", "Green", [])

    def test_initialization(self, bubble_tea):
        assert bubble_tea.name == "Test Tea"
        assert bubble_tea.size == "Large"
        assert bubble_tea.level_of_ice == "Full"
        assert bubble_tea.level_of_sugar == "Full"
        assert bubble_tea.green_or_black_tea == "Green"
        assert bubble_tea.toppings == []

    # testing the add and remove toppings functions
    def test_add_topping(self, bubble_tea):
        bubble_tea.add_topping("Pearls")
        assert "Pearls" in bubble_tea.toppings

    def test_remove_topping(self, bubble_tea):
        bubble_tea.add_topping("Pearls")
        bubble_tea.remove_topping("Pearls")
        assert "Pearls" not in bubble_tea.toppings
