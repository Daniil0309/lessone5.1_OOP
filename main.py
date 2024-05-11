#Наследование
class Bird():
    # Определение класса Bird
    def __init__(self, name, voice, color):
        # Метод инициализации объекта класса Bird
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        # Метод для вывода сообщения о полете птицы
        print(f"{self.name} летает")

    def eat(self):
        # Метод для вывода сообщения о том, что птица ест
        print(f"{self.name} ест")

    def sing(self):
        # Метод для вывода сообщения о пении птицы
        print(f"{self.name} поет - курлык")

    def info(self):
        # Метод для вывода информации о птице (имя, голос, цвет)
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - цвет")

class Pigeon(Bird):
    # Класс Pigeon наследует класс Bird
    def __init__(self,name, voice, color, favorite_food):
        # Метод инициализации объекта класса Pigeon
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        # Переопределенный метод для пения голубя
        print(f"{self.name} поет - гав ")

    def walk(self):
        # Метод для вывода сообщения о ходьбе голубя
        print(f"{self.name} гуляет")

bird1 = Pigeon("Рыжик", "кря-кря", "красный", "мясо")
# Создание объекта bird1 класса Pigeon с передачей аргументов
bird2 = Bird("Кеша", "кря-кря", "черный")
# Создание объекта bird2 класса Bird с передачей аргументов

bird1.sing()
# Вызов метода sing() для объекта bird1
bird1.info()
# Вызов метода info() для объекта bird1
bird1.walk()
# Вызов метода walk() для объекта bird1

bird2.sing()
# Вызов метода sing() для объекта bird2

