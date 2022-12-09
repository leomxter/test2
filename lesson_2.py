#Операторы сравнения, функция input(), условаия if и else, boolean, циклы
# ==, >=, <=, <, >, !=
# print(10==9)
# print(10==10)
# print("IT" == "IT")
# print(10.0 == 10.0)
# print(2 == 2.0)
# print(False == False)
# print(10 == "10")
# print(int("10") == 10)
# print(10 > 20)
# print(10 < 5)
# print(10 != 9)
# print(1000 != 1000)
# print(50 >= 50)
# print(100 >= 50)
# print(30 >= 100)
# print(30 <= 400)

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите второе число: "))
# print(num1 + num2)

# name = input("Введите имя:")
# print("Здравствуйте", name)

#if, else, elif
# if True:
#     print("if true")
# else:
#     print("if false")
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# if num1 > num2:
#     print("первое число больше")
# else:
#     print("второе число больше")

# num = int(input("введите число: "))
# if num % 2 == 0:
#     print(num, "четный")
# else:
#     print(num, "нечетный")

#Логические операторы or и and
# num1 = 100
# num2 = 100
# num3 = 100
# if num1 > num2 and num1 > num2:
#     print("первое число больше")
# elif num2 > num1 and num2 > num3:
#     print("второе число больше")
# elif num3 > num1 and num3 > num2:
#     print("третье число больше")
# else:
#     print("они равны")

# login = input("введите логин: ")
# password = input("введите пароль: ")
# if login == "LeoMxter" and password == "123blackmongol":
#     print("Welcome")
# else:
#     print("Error")

# login = input("введите логин: ")
# password = input("введите пароль: ")
# if login == "MeGun":
#     if password == "123blackmongol":
#         print("Welcome")
#     else:
#         print("password is incorrect")
# else:
#     print("login is incorrect")
# while True:
#     num1 = float(input("введите первое число: "))
#     num2 = float(input("введите второе число: "))
#     oper = input("+, -, *, /: ")
#     if oper == "+":
#         print(num1 + num2)
#     elif oper == "-":
#         print(num1 - num2)
#     elif oper == "*":
#         print(num1 * num2)
#     elif oper == "/":
#         print(num1 / num2)
#     else:
#         print("Error")

# print(True + False) #True = 1, False = 0

# Циклы for и while
# for num in range(1001):
#     print(num)
# name = "Elmo"
# for i in name:
#     print(i)
#     if i == 'l':
#         print("there is l in a name")                      
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)