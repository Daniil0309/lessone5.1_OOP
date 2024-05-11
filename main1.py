#Инкапсуляция это работа с атрибутами

class Test():
    # Определение класса Test
    def __init__(self):
        # Метод инициализации объекта класса Test
        self.public = ("публичный атрибут")
        # Публичный атрибут класса
        self._protected = "защищенный атрибут"
        # Защищенный атрибут класса
        self.__private = "приватный атрибут"
        # Приватный атрибут класса

    def get_private(self):
        # Метод для получения значения приватного атрибута
        return self.__private

    def set_private(self, value):
        # Метод для установки значения приватного атрибута
        self.__private = value

test = Test()
# Создание объекта test класса Test
print(test.public)
# Вывод публичного атрибута
print(test._protected)
# Вывод защищенного атрибута
print(test.get_private())
# Вывод приватного атрибута с помощью метода get_private()
test.set_private("новый приватный атрибут")
# Изменение значения приватного атрибута с помощью метода set_private()
print(test.get_private())
# Вывод измененного приватного атрибута с помощью метода get_private()

