# def print(name):
#     print(f'{name} its may name')

# print('Elmo')
# print('Elmyrza')
 
class Human:
    # Атрибут уровня класса
    head = 1
    hand = 2
    # конуструктор класса
    def __init__(self,name,age):
        self.name = name
        self.age = age
human = Human('Elmyrza', 14)
print(human.name, human.age)
print(human.head)
human2 = Human('Nurislam', 14)
print(human2.name, human2.age)
print(human2.head)  

elmo = Human('Elmo')
elmo.print()
num2 = Human('Nuris')
print(num2.print(), num2.age)


# class Car:
#     motor = 1
#     def __init__(self, model,age,mark):
#         self.model = model
#         self.age = age
#         self.mark = mark
#     def __str__(self):
#         return f'Model: {self.model}, Age: {self.age}, Mark: {self.mark}'

# car1=Car('bmw', 2010,  'x5')
# print(car1)

# car2 = Car('mersedes', 2021, 'S')
# print(car2)

