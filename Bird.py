from Animal import Animal


class Bird(Animal):
    def __init__(self, name: str = 'noname', color: str = None, size: str = None):
        super().__init__(name)
        self.color = color
        self.size = size

    def get_info(self) -> str:
        return f'Bird name: {self.name}, color: {self.color}, size: {self.size}'
