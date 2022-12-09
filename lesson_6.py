#Лямбда функции, исключения try, except
# def hello_world():
#     return "Hello World"
# print(hello_world())

# def mult(num):
#     return num * num
# print(mult(10))

# lambda_mult = lambda num: num * num #mini function
# print(lambda_mult(10))
# print((lambda num: num * num)(10))

# def add(num1 : int, num2 :int):
#     return num1 + num2
# print(add(20, 50))

# lambda_add = lambda num1, num2: num1 + num2
# print(lambda_add(20, 50))

# print((lambda num1, num2: num1 + num2)(20, 50))

# def geektech(word):
#     return word
# print(geektech("geektech"))

# lam_geek = lambda word: word
# print(lam_geek("Lambda GeekTech"))
# print((lambda word: word)("GeeKTech lambda"))

# a = [1, 2, 3, 4, 5]
# def mult_2(lst : list):
#     res = []
#     for i in lst:
#         res.append(i * 5)
#     return res
# print(mult_2(a))

# ##########################

# a = [1, 2, 3, 4, 5]
# res = list(map(lambda lst: lst * 5, a))
# print(res)
# ####################
# a = [1, 2, 3, 4, 5]
# print(list(map(lambda lst: lst * 5, a)))
# ####################
# print(list(map(lambda lst: lst * 5, [1, 2, 3, 4, 5])))
# a = [2, 5, 8, 9, 10, 6]
# def chet(lst_nums : list):
#     res = []
#     for num in lst_nums:
#         if num % 2 == 0:
#             res.append(num)
#         else:
#             pass
#     return res
# print(chet(a))
# ##################
# res = list(filter(lambda lst_nums: lst_nums % 2 == 0, a))
# print(res)
# ##################
# print(list(filter(lambda lst_nums: lst_nums % 2 == 0, [2, 5, 8, 9, 10, 6])))

# try:
    # print(10 / 0)
# except ZeroDivisionError:
    # print('Деление на ноль')

# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#     except ValueError:
#         print("Вводи целые числа")
#     operator = input("+ - * /: ")
#     if operator == "+":
#         print(num1 + num2)
#     elif operator == "-":
#         print(num1 - num2)
#     elif operator == "*":
#         print(num1 * num2)
#     elif operator == "/":
#         try:
#            print(num1 / num2)
#         except ZeroDivisionError:
#             print("Ошибка. На ноль не делится")
#     else:
#         print("Оператор не найден")
