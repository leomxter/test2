# print(10 + 10.0)
# print(10 + "10") #error
# print(100 + True + False) #101
# print(True + False) #1

# list - список
# lst = [1, 20.0, "Hello", True, [1, 2, 3]]
# print(lst)

# name1 = "Elmyrza"
# name2 = "Askhat"
# name3 = "Arsor"
# print(name1)
# print(name2)
# print(name3)
# names = ["Elmyrza", "Askhat", "Arsor"]
#          #  0          1         2
# names.append("Abror") #добавление элемента в конец списка
# print(names)
# print(names[0])
# print(names[0:3:2])

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num[0:5:4])
# print(num[1:4:2])
# print(num[0:7:3])
# print(num[0:9:8])
# print(num[1:9:7])
# it_comp = ["Meta", "Google", "Mad Devs", "Hapsida"]
# print(it_comp)
# it_comp.insert(0, "Microsoft") #Вставка по индексу
# print(it_comp)
# it_comp.insert(2, "UbiSoft")
# print(it_comp) 
# it_comp.remove("Meta") #удаление элемента по значении
# print(it_comp)
# it_comp.pop() #Удаление последнего элемента из списка
# print(it_comp)
# it_comp.pop(2) #Удаление по индексу
# print(it_comp)
# del it_comp[0] #Второй спсоб удаления по индексу
# print(it_comp)
# it_comp[0] = "GeekTech"
# print(it_comp)
# it_comp[1] = "UbiSoft"
# print(it_comp)

# cars = ["BMW", "Lexus", "Toyota", "Ferrari", "Tesla"]
# print(cars)
# # print(cars[::-1]) #первый способ перевернуть список
# # res = list(reversed(cars)) 
# # print(res) #второй способ перевернуть список
# print(cars.index("Toyota")) 
# print(cars.index("Tesla"))
# del cars[0:3:2] 
# print(cars)

#Агрегатные функции max, min, sum
# price =  [100, 500, 300, 100, 255, 600, 700, 10]
# print(price)
# print(min(price)) #Минимальное значение
# print(max(price)) #Максимальное значение
# print(sum(price)) #Общяя сумма всех чисел

#Сортировка списков
# price.sort()
# print(price)
# price.sort(reverse=True)
# print(price)
# number = [1, 56, 2.0, 4.0, 4]
# number.sort()
# print(number)

# cars = ["BMW", "Lexus", "Toyota", "Ferrari", "Tesla"]
# cars.sort()
# print(cars)
# contacts = ["Askhat", "Daniel", "Janboto"]
# find_contact = input("Имя: ").title()
# if find_contact in contacts:
#     print(find_contact, "найден")
# else:
#     print(find_contact, "не найден")
# name = "elMyRzA"
# print(name.title())
# print(name.upper())
# print(name.lower())
# name = [1, 2, 3] #переменная переприсвоена 
# print(name)

