from Animal import Animal


class Dog(Animal):
    def __init__(self, name: str = 'noname', color: str = None, age: int = None):
        super().__init__(name)
        self.color = color
        self.age = age

    def get_info(self) -> str:
        return f'Dog name: {self.name}, color: {self.color}, age: {self.age}'
