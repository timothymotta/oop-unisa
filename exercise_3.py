#  Create a class for a car. It should contain properties such as make, model and
#  year. It should also have a method which displays all its information.

class Car:
     def __init__(self):
      self.make = "Jaguar"
      self.model = "XE" 
      self.year = "2024"

     def display_information(self):
         print("Car Info: \n", self.make, self.model, self.year)