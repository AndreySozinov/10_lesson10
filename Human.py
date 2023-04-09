# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.
class Human:
    def __init__(self, surname: str, name: str, patronymic: str, age: int, sex: str):
        self.surname = surname
        self. name = name
        self.patronymic = patronymic
        self.__age = age
        self.sex = sex

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def full_name(self):
        return f'{self.surname} {self.name} {self.patronymic}'


if __name__ == '__main__':
    h1 = Human('Petrov', 'Ivan', 'Andreevich', 28, 'male')
    print(h1.full_name())
    print(h1.get_age())
    h1.birthday()
    print(h1.get_age())
    