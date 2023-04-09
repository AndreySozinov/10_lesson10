# Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:
    def __init__(self, radius: int | float):
        self.radius = radius

    def length(self) -> float:
        return 2 * pi * self.radius

    def area(self) -> float:
        return pi * self.radius ** 2


if __name__ == '__main__':
    c1 = Circle(4)
    print(c1.length())
    print(c1.area())
