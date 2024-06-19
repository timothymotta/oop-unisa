'''
File: store.py
Description: This is the store class which is the main hub for ordering tea. It stores the order history and it also contains all the price information.
Author: Timothy Motta
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''
from fruittea import FruitTea
from milktea import MilkTea
from sparklingtea import SparklingTea
from hottea import HotTea
from frozentea import FrozenTea
from topping import Topping

class Store:
    def __init__(self):
        self.earnings = 0.0
        self.orders = []
        self.prices = {
            "BASE PRICE": 4.5,
            "SIZE OF TEA": {
                "Small": 0.0,
                "Medium": 0.85,
                "Large": 1.2,
            },
            "TYPE OF TEA": {
                "Fruity": 0.15,
                "Milky": 0.29,
                "Sparkling": 0.19,
                "Hot": 0.24,
                "Frozen": 3.0,
            },
            "FRUITS": {
                "Mango": 0.3, "Lychee": 0.1, "Apple": 0.2,
                "Grape": 0.4, "Melon": 0.5, "Grapefruit": 0.1,
                "Lemon": 0.3, "Guava": 0.2, "Passionfruit": 0.25,
                "Strawberry": 0.2, "Pomegranate": 0.45, "Peach": 0.1,
                "Tropical": 0.65, "Watermelon": 0.35,
            },
            "FLAVOURS": {
                "Mint Choc": 0.3, "Thai": 0.35, "Salted Caramel": 0.2,
                "Roasted": 0.4, "Earl Grey": 0.5, "Vanilla": 0.1,
                "Assam": 0.3, "Hazelnut": 0.2, "Oolong": 0.25,
                "Jasmine": 0.2, "Matcha": 0.45, "Taro": 0.65,
                "Chocolate": 0.4,
            },
            "TOPPINGS": {
                "Custard": 1.0, "Mousse": 2.4, "Pearls": 1.2,
                "Cookie Crumb": 0.75, "Mixed Jellies": 0.35, "Herbal Jelly": 0.45,
                "Coconut Jelly": 0.5, "Aloe Vera": 0.7, "Mango Popping Pearls": 0.4,
                "Strawberry Popping Pearls": 0.4, "Apple Popping Pearls": 0.4,
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
        return f"TOTAL EARNINGS: \n${self.earnings:.2f}, \n\nTOTAL ORDERS: \n{len(self.orders)}\n"