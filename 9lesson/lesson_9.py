# def chet(number : int = 0) -> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(chet(4))

# while True:
#     name = input('Your name: ')
#     print(name)

# def while_true():
#     while True:
#         name = input('your name: ')
#         print(name)

# def lambda_function():
#     number = [1, 2, 3, 4, 5, 6, 7, 8]
#     return tuple(filter(lambda lst_num : lst_num % 2 == 0, number))
# print(lambda_function())

# num1 = 10
# num2 = 20
# number = 13
# def nearer_num(num1, num2, number):
#     num1_abs = abs(number - num1)
#     num2_abs = abs(number - num2)
#     # if num1_abs < num2_abs:
#     #     return num1
#     # elif num2_abs < num1_abs:
#     #     return num2
#     # else:
#     #     return "Равны"
#     return num1 if num1_abs < num2_abs else num2 if num2_abs < num1_abs else 'Равны' 
# print(nearer_num(num1, num2, number))

# print(abs(-10))  #изменение отрицательного числа в положительный

# lambda_chet = lambda number: number % 2 == 0
# print(lambda_chet(3))

# def count_words(words : str):
#     split_words = words.replace(",", "").lower().split()
#     res = {}
#     for word in split_words:
#         res[word] = split_words.count(word)
#     return res 

# print(count_words("Money, money, money, it's always sunny, in the richmen's world"))
