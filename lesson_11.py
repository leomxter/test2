# class H:
#     atribut = 1
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def run(self):
#         print('run')

# g = H('name', 19)
# g.run()
##################
# объектное орентирование программирования
# населдование инкапсуляции
# git
# супер класс == главный класс
class Human:
    head = 1
    def __init__(self, name,age, lastname):
        self.name = name 
        self.age = age
        self.lastname = lastname
    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'lastname is {self.lastname}'
    def run(self):
        print(f'{self.name} is running')

hum = Human('Elmyrza', 15, 'Doolotbekov')
print(hum)

# Дочерний класс
class Student(Human):
    head = 2
    def __init__(self,name,age, lastname):
        super().__init__(name,age, lastname)
        Human.__init__(self,name,age, lastname)
        self.lastname = lastname
    def fly(self):
        print(self.name, 'is fly in True')
    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'lastname is {self.lastname}'

student = Student('Daniyel', 60, 'Ermekov')
print(student)
# print(student)
# print(student.run)
# student.run()
# student.fly()

# Дочерний класс
class Teacher(Student):
    def fly(self):
        print(f'{self.name} is flying')

tech = Teacher('Elmo', 55, 'Doolotbekov')
tech.fly()
tech.run()

# class Robot:
#     def noSleep(a):
#         print(f'{a} function no Sleep True')

# class Robot2(Robot):...

# Robot.noSleep(student.name)


