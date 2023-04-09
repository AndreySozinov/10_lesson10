# Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
import Animal
from Bird import Bird
from Dog import Dog
from Fish import Fish


class Fabric:
    @staticmethod
    def generate(animal_type: str, name: str = 'noname', color: str = None,
                 predator: bool = False, size: str = None, age: int = None) -> Animal:
        match (animal_type.lower()):
            case 'fish':
                return Fish(name, color, predator)
            case 'bird':
                return Bird(name, color, size)
            case 'dog':
                return Dog(name, color, age)


if __name__ == '__main__':
    a1 = Fabric.generate('Bird', name='Orlusha', color='black', size='small')
    a2 = Fabric.generate('Fish', color='silver', predator=True)
    a3 = Fabric.generate('Dog', name='Butch', color='red', age=3)

    print(type(a1), type(a2), type(a3))
    print(a1.get_info())
    print(a2.get_info())
    print(a3.get_info())
