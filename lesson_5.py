# Функции
# def calc():
#     numb1 = int(input("Введите первое число: "))
#     numb2 = int(input("Введите второе число: "))
#     print(numb1 + numb2)
# calc() #Вызов функции

# def hello_world():
#     print("Hello World")
#     def test():
#         print("Testing")
#     test()
# hello_world()
# def add(num1, num2):
#     print(num1 + num2)
# add(20, 30)
# add(-20, 40)
# add(200, 50)
# add(20, -60)

# def chet(number):
#     if number % 2 == 0:
#         print(number, "четное")
#     else:
#         print(number, "нечетное")
# chet(30)

# def input():
#     print("Hi")
# input()

# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mult(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1 / num2

# def main(number1, number2, operator):
#     if operator == "+":
#         return add(number1, number2)
#     elif operator == "-":
#         return sub(number1, number2)
#     elif operator == "*":
#         return mult(number1, number2)
#     elif operator == "/":
#         return div(number1, number2)
#     else:
#         return "Operator not found"
# print(main(30, 15, "/"))
# print(main(30, 20, "*"))
# print(main(30, 10, "-"))
# print(main(30, -10, "+"))

# def number(num):
#     return int(str(num)[::-1])
# print(number(342))

# numbers = ['1', '2', '3', '4']
# print(numbers)
# res = str().join(numbers) #Объединение
# print(type(res))
# lst = []
# for num in numbers:
#     lst.append(int(num)):
# print(lst)
# def reverse(num):
#     print(tuple(num[::-1]))
# reverse([1, 2, 3, 4, 5])

# def add(num1 = 10, num2 = 30): #Значение по умолчанию
#     return num1 + num2
# print(add(40)) #Примет 40 за num1, получается num1 + num2 = 70
 
def add(num1 : int  = 10, num2 : int = 30):
    return num1 + num2
print(add(num2=60))
