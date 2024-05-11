class Car:
    # Определение класса Car
    def __init__(self, make, model):
        # Метод инициализации объекта класса Car
        self.public_make = make
        # Публичный атрибут make
        self._protected_model = model
        # Защищенный атрибут model
        self.__private_year = 2022
        # Приватный атрибут year

    def public_method(self):
        # Публичный метод, возвращающий строку с использованием атрибутов make и model
        return f"Это публичный метод. Машина {self.public_make} {self._protected_model}"

    def _protected_method(self):
        # Защищенный метод, возвращающий строку
        return "Это защищеный метод"

    def __private_method(self):
        # Приватный метод, возвращающий строку
        return "Это приватный метод."

class ElectricCar(Car):
    # Подкласс ElectricCar, наследующий от Car
    def __init__(self, make, model, battery_size):
        # Метод инициализации объекта класса ElectricCar
        super().__init__(make, model)
        # Вызов метода инициализации родительского класса
        self.battery_size = battery_size
        # Атрибут battery_size

    def get_details(self):
        # Метод для получения деталей автомобиля
        details = f"{self.public_make} {self._protected_model}, Батарея: {self.battery_size} Kwh."
        return details
        # Возвращение строки с деталями

# Создаем экземпляр ElectricCar
tesla = ElectricCar("Tesla", "Model S", 100)

# Доступ к открытому атрибуту и методу
print(tesla.public_make)
print(tesla.public_method())

# Доступ к защищенному атрибуту и методу (не рекомендуется, но возможно)
print(tesla._protected_model)
print(tesla._protected_method())

# Доступ к приватному атрибуту и методу напрямую невозможен, но Python позволяет обойти это ограничение (не рекомендуется)
print(tesla._Car__private_year) # Доступ к приватному атрибуту через name mangling

