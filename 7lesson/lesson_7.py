def mult(num1 : int, num2 : int) -> int:
    return num1 * num2
# print(mult(20, 20))

def div(num1 : int, num2 : int) -> float:
    try:
        return num1 / num2
    except:
        return "Деление на ноль"
# print(div(30, 20))

it = "GeekTech"
numbers = [10, 20, 30, 40, 50]
number = 415
name = "Elmyrza"

import random
print(random.randint(1, 5)) 

def random_number():
    num_random = random.randint(1, 10)
    n = 0
    while True:
        try:
            user_input = int(input("Text number from 1 to 10: "))
            n += 1
            if num_random == user_input:
                print(f"Correct answer. Number {num_random}")
            elif n == 5:
                print("Attempts run out")
                break
            elif user_input > 10:
                print("Text numbers under 10")
            elif user_input < 1:
                print("Text numbers more than 0")
            else:
                print(f"Incorrect, {5 - n} attempts")
        except ValueError:
            print("I accept only integer")
# random_number()
# raise ImportError("Hello World!") #вызов ошибки   