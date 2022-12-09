#инкапсуляция заключение в одно место(класс) для работы с ними
#public без нижних подчеркиваний
#private
class Human:
    head = 1
    def __init__(self, name,age):
        self._name = name 
        self.age = age
    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}'
    def run(self):
        print(f'{self.name} is running')
def run(a):
    print(f'{a} is running')

h = Human('Nurislam', 14)
h.name = 'Elmo' #changing the name of Human
h._name = 'Baisal'
# print(h._name) #saved name
# h.__name = 'Janboto'
print(h.name, h._name)
h.run()