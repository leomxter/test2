# f = open('geektech.txt', 'w') 
# f.write("Hello World!")
# f.close()

# r = open('geektech.txt', 'r') #вывод данных в терминале
# print(r.read())
# r.close()

# code = open('lesson_7.py', 'r')
# print(code.read())
# code.close()

# pyt = open('hello.py', 'w')
# pyt.write("print('Hello World!')")
# pyt.close()

# student = open('student.txt', 'w')
# student.write('Askhat\n')
# student.write('Daniel\n')
# student.close()

# student_1 = open('student.txt', 'a+') #добавление элемента в список
# student_1.write('Almaz')
# student_1.close()

# with open('python.txt', 'w') as f: 
#     f.write("Python 3.8.10")

# with open('python.txt', 'r') as r:
#     print(r.read())
# import os

# n = 0
# while True:
#     n+=1
#     if n == 10:
#         break
#     else:
#         with open(f'python_{n}.py', 'w') as f:
#             f.write("Hello World")
# n = 0
# while True:
#     n+=1
#     if n == 10:
#         break
#     else:
#         os.remove(f'python_ + {n}.py')
# import os

# txt = open('login.txt', 'w')
# txt.write('login: leomxter\n')
# txt.write('password: blackclover')
# txt.close

# login = open('login.py', 'w')
# login.write(input('login: \n'))
# login.write(input('password: '))
# login.close()

# reg = open('reg.py', 'w')
# if login == txt:
#     reg.write('password and login are correct')
# reg.close()


# def write_login_password(login, password): 
#     with open('password.txt', 'w') as o:
#         o.write(f'{login} {password}')
# write_login_password('geektech', 'geektech2021')
# import datetime
# time = datetime.datetime.now()

# def read_login_password(login : str, password : str) -> bool:
#     with open('password.txt', 'r') as r:
#         result = r.read().split()
#     if login.lower() == result[0] and password == result[1]:
#         with open('logs.txt', 'a+') as logs:
#             logs.write(f'{login.lower()} {time.ctime()}\n')
#         return True
#     else:
#         return False

import random

def generate_passwords() -> str:
    res=[]
    password = []
    letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for i in letters:
        res.append(i)
        print(res)
        print(random.choices(res))
    for n in range(10):
        password = []
        for i in range(8):
            password.append("".join(random.choices(res)))
        with open('generated_password.txt', 'a+') as p:
                p.write(f'{"".join(password)}\n')

generate_passwords()