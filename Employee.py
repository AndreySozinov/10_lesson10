# Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
from Human import Human


class Employee(Human):
    divider = 7

    def __init__(self, employee_id: int, surname: str, name: str, patronymic: str, age: int, sex: str):
        super().__init__(surname, name, patronymic, age, sex)
        self.id = employee_id
        self.access_level = sum(int(digit) for digit in str(self.id)) % self.divider


if __name__ == '__main__':
    e1 = Employee(641250, 'Ivanov', 'Ivan', 'Jhonovich', 34, 'male')
    print(e1.full_name())
    print(e1.access_level)
