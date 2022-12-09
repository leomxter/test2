#Tuple - Кортеж
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.append(7)
# print(numbers)
# numbers.remove(2)
# print(numbers)
# numbers[0] = "One" #Изменение элемента в списке
# print(numbers)

# numbers = (1, 2, 3, 4, 5)
# for num in numbers:
#     print(num)
# print(numbers)
# numbers.remove(1)
# print(numbers)
# numbers.pop(1)
# print(numbers)
# del numbers[0]
# print(numbers)

# numbers[0] = "One"
# print(numbers)
# print(numbers[0])
# print(numbers[0:3:2])
# print(numbers.count(3))
# print(numbers.index(3))

# cities = ["Osh", "Bishkek", "Talas"]
# tup_cities = tuple(cities)
# print(tup_cities)
# lst_cities = list(cities)
# print(lst_cities)
# lst_cities.append("Naryn")
# tup_cities = tuple(lst_cities)
# print(tup_cities)

#множество set, frozenset
# a = [1, 3, 4, 5]
# b = [2, 4, 5, 6, 7]
# print(list(set(a + b)))

# st = {1, 1.0, True, "1", (1, 2, 3)} 
# print(st)

# cars = {"BMW", "LEXUS", "TOYOTA", "BMW"}
# print(cars[0]) #по индексу в set ничего не выводится
# print(cars)
# cars.add("Ferrari")
# print(cars)
# cars.remove("LEXUS")
# print(cars)
# cars.pop() #set не принимает индексы
# print(cars)
# for car in cars:
#     print(car)

# number = {10, 20, 30, 40}
# frzn_number = frozenset(number)
# print(frzn_number)

#dict - словари
# n = {1, 2, 3, 4, 5}
# print(len(n))
# student = {'name' : 'Elmyrza', 'age' : 14} 
# print(student)
# print(len(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('work', 'GeekTech') #добавление элемента
# print(student)
# student.pop('name')
# print(student)
# print(student.keys()) #вывод ключей
# print(student.values()) #вывод значений
# print(student.items()) #разделение элементов
# student['age'] = 15 #обновление значения элемента
# student['test'] = 16
# print(student) 
# del student['test']
# print(student)
# for k, v in student.items():
#     print(k, v) #вывод ключей и значений отдельно
contact = {"MCHS" : 112}
while True:
    command = input("1 - show all contacts, 2 - add contact, 3 - remove contact, 4 - update contact: ")
    if command == "1":
        for name, number in contact.items():
            print(name, number)
    elif command == "2":
        add_name = input('Text new name: ')
        add_number = input('Text new number: ')
        contact.setdefault(add_name, add_number)
        print('Contact was successfully added')
    elif command == "3":
        delete_contact = input("Text contact's name to remove: ")
        if delete_contact in contact.keys():
            del contact[delete_contact]
            print('contact was successfully removed')
        else:
            print('Not found')
    elif command == "4":
        up_contact = input("Contact's name to update: ")
        if up_contact in contact:
            print("Contact was found")
            up_num = input("Updated number: ")
            contact[up_contact] = up_num
        else:
            print("Contact wasn't found")           