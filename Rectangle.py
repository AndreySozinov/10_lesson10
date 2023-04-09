# Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
class Rectangle:
    def __init__(self, length: int | float, width=0):
        self.length = length
        if not width:
            width = length
        self.width = width

    def perimeter(self) -> int | float:
        return 2 * self.length + 2 * self.width

    def area(self) -> int | float:
        return self.length * self.width


if __name__ == '__main__':
    r1 = Rectangle(5, 2)
    print(r1.perimeter())
    print(r1.area())
