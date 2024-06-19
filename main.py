'''
File: main.py
Description: This is the main file which runs and displays the code.
Author: Timothy Motta
ID: 110401113
Username: motty001
This is my own work as defined by the University's Academic Misconduc Policy.
'''

from store import Store
from topping import Topping
from fruittea import FruitTea
from milktea import MilkTea
from sparklingtea import SparklingTea
from hottea import HotTea
from frozentea import FrozenTea

def main():
    store = Store()

    # toppings
    custard_topping = Topping("Custard", store.prices)
    mousse_topping = Topping("Mousse", store.prices)
    pearls_topping = Topping("Pearls", store.prices)
    cookie_topping = Topping("Cookie Crumb", store.prices)
    mixed_jellies_topping = Topping("Mixed Jellies", store.prices)
    herbal_jelly_topping = Topping("Herbal Jelly", store.prices)
    coconut_jelly_topping = Topping("Coconut Jelly", store.prices)
    aloe_vera_topping = Topping("Aloe Vera", store.prices)
    mango_popping_pearls_topping = Topping("Mango Popping Pearls", store.prices)
    strawberry_popping_pearls_topping = Topping("Strawberry Popping Pearls", store.prices)
    apple_popping_pearls_topping = Topping("Apple Popping Pearls", store.prices)

    print("|=================================================================================================|\n")
    print("|                    ░█▀▀█ ░█─░█ ░█▀▀█ ░█▀▀█ ░█─── ░█▀▀▀ 　 ▀▀█▀▀ ░█▀▀▀ ─█▀▀█                     |")
    print("|                    ░█▀▀▄ ░█─░█ ░█▀▀▄ ░█▀▀▄ ░█─── ░█▀▀▀ 　 ─░█── ░█▀▀▀ ░█▄▄█                     |")
    print("|                    ░█▄▄█ ─▀▄▄▀ ░█▄▄█ ░█▄▄█ ░█▄▄█ ░█▄▄▄ 　 ─░█── ░█▄▄▄ ░█─░█                     |\n")
    print("|=================================================================================================|")

    # ordering teas
    store.order_tea(FruitTea, "Tropical Fruit Tea", "Large", "Regular", "Full", "Green", [apple_popping_pearls_topping])
    store.order_tea(MilkTea, "Classic Milk Tea", "Medium", "Less", "Half", "Black", [custard_topping])
    store.order_tea(SparklingTea, "Sparkling Lemon Tea", "Small", "Full", "Full", "Green", [mixed_jellies_topping])
    store.order_tea(HotTea, "Hot Earl Grey Tea", "Large", "None", "None", "Black", [mousse_topping])
    store.order_tea(FrozenTea, "Frozen Mango Tea", "Medium", "Regular", "Full", "Green", [mango_popping_pearls_topping])
    store.order_tea(FruitTea, "Mango Coconut Fruit Tea", "Large", "Regular", "Full", "Green", [mango_popping_pearls_topping, coconut_jelly_topping])
    store.order_tea(MilkTea, "Classic Cookie Milk Tea", "Medium", "Less", "Half", "Black", [cookie_topping])
    store.order_tea(SparklingTea, "Sparkling Herbal Lemon Tea", "Small", "Full", "Full", "Green", [pearls_topping, herbal_jelly_topping] )
    store.order_tea(HotTea, "Hot Earl Grey Mousse Tea", "Large", "None", "None", "Black", [mousse_topping])
    store.order_tea(FrozenTea, "Frozen Aloe Vera Strawberry Tea", "Medium", "Regular", "Full", "Green", [aloe_vera_topping, strawberry_popping_pearls_topping])

    # display store
    print(store)
    store.view_order_history()

if __name__ == "__main__":
    main()
