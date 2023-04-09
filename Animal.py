# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
class Animal:
    def __init__(self, name: str = 'noname'):
        self.name = name

    def get_info(self) -> str:
        return f'Animal name: {self.name}'