# Создаём класс машина:
from unicodedata import name


class Car:
    # Создадим атрибут класса:
    
    car_count = 0
    
    # Создадим атрибуты класса:
    name = 'Mercedez-Benz'
    model = 'c300'
    release = 2008
    @staticmethod # Статический метод, ставим Дескриптор или синтаксический сахар
    def get_class_details():
        print('Это класс Car')
    def __init__(self): # Конструктор
        Car.car_count += 1
        print(Car.car_count)
    # Создаём метод класса:
    def __str__(self): # Переопределяем метод __str__, предоставив наше собственное определ. метода
        return 'Car class object'
    
    def start(self, name, model, release):
        print('Заводим двигатель')
        self.name = name # Атрибут экземпляра
        self.model = model # Атрибут экземпляра
        self.release = release # Атрибут экземпляра
        Car.car_count += 1
    
    def stop(self):
        print('Глушим двигатель') 

car_a = Car()
car_b = Car()
car_c = Car()       
# Создаем  два обьекта класса Car:
# car_a = Car()
# car_a.start('Corrola', 'Toyota', 2015)
# print(car_a.name)
# print(car_a.model)
# print(car_a.release)
# print(car_a.car_count)

# car_b = Car()
# car_b.start('Honda', 'Accord', 2007)
# print(car_b.model)
# print(car_b.name)
# print(car_b.release)
# print(car_b.car_count)
# Car.get_class_details()
#print(dir(car_b))

# class Square:
    
#     @staticmethod
#     def get_squares(a, b):
#         return a*a, b*b
# print(Square.get_squares(3, 5))    
# car_a = Car()
# print(car_a)