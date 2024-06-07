from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    def __init__(self):
        self.__area = self.calculate_area()

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    area = property(get_area, set_area)

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def scale(self, factor):
        pass

    def __str__(self):
        return f" This shape has an area of {round(self.area, 2)}."


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().__init__()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    width = property(get_width)
    height = property(get_height)

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def scale(self, factor):
        self.__width *= factor
        self.__height *= factor
        self.area = self.calculate_area()

    def __str__(self):
        return f"A rectangle with a width of {self.__width} and height of {self.__height}." + super().__str__()


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
        super().__init__()

    def get_radius(self):
        return self.__radius

    radius = property(get_radius)

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

    def scale(self, factor):
        self.__radius *= factor
        self.area = self.calculate_area()

    def __str__(self):
        return f"A circle with a radius of {self.__radius}." + super().__str__()


class Triangle(Shape):
    def __init__(self, hypotenuse, opposite, adjacent):
        self.__hypotenuse = hypotenuse
        self.__opposite = opposite
        self.__adjacent = adjacent
        super().__init__()

    def get_hypotenuse(self):
        return self.__hypotenuse

    def get_opposite(self):
        return self.__opposite

    def get_adjacent(self):
        return self.__adjacent

    hypotenuse = property(get_hypotenuse)
    opposite = property(get_opposite)
    adjacent = property(get_adjacent)

    def calculate_area(self):
        semi_perimeter = self.calculate_semi_perimeter()
        return sqrt(semi_perimeter * (semi_perimeter - self.__hypotenuse)
                    * (semi_perimeter - self.__opposite)
                    * (semi_perimeter - self.__adjacent))

    def calculate_perimeter(self):
        return self.__hypotenuse + self.__opposite + self.__adjacent

    def calculate_semi_perimeter(self):
        return (self.__hypotenuse + self.__opposite + self.__adjacent) / 2

    def scale(self, factor):
        self.__hypotenuse *= factor
        self.__opposite *= factor
        self.__adjacent *= factor
        self.area = self.calculate_area()

    def __str__(self):
        return f"A triangle with the sides {self.__hypotenuse}," \
            f"{self.__opposite}, and {self.__adjacent}." + super().__str__()