from Animal import Animal


class Fish(Animal):
    def __init__(self, name: str = 'noname', color: str = None, predator: bool = False):
        super().__init__(name)
        self.color = color
        self.predator = predator

    def get_info(self) -> str:
        return f'Fish name: {self.name}, color: {self.color}, predator: {self.predator}'
