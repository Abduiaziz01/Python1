# #Списки - list
# #4 str, int, float, bool, list
# # print("10" + 5)
# # name1 = "Kurmanbek"
# # name2 = "Syimyk"
# # name3 = "Beksultan"
# # name4 = "Nurbolot"
# # print(name1, name2, name3, name4)

# # names = ["Kurmanbek", "Syimyk", "Beksultan", "Nurbolot" ]
# # print(names)
# # list = [10, 0.1, "Geeks", False]
# # print(list)

# # it = ["Google", "Amazon", "Mad Devs"]
# # print(it)
# # it.append("GeeksStudio") #метод append добавляет в конец списка значения
# # print(it)
# # it.append("Apple")
# # print(it)
# # it.remove("Amazon") #метод remove удалят значения из списка
# # print(it)
# # # it.remove("Bayas") #если значения которую нужно удалить в списке нету, то выводится ошибка
# # # print(it)

# # cars = ["BMW", "Tesla", "BYD", "Mercedes"]
# #           #0       1       2        3
# # print(cars)
# # print(cars[1])
# # print(cars[1][2])
# # print(cars[1:3]) #в списках можно использовать срезы и индексы
# # cars[2] = "Zeekr" #обновление значение из списка с помощью индекса
# # print(cars)
# # cars.pop(2) #метод pop удаляет из списка по индексу
# # print(cars)

# # numbers = [101, 202, 506, 702, 1001]
# # print(numbers)
# # numbers.insert(0, "Abu") #метод insert добавлят значение по индексу
# # print(numbers)
# # del numbers[0] #оператор del удаляет значение по индексу и срезу
# # print(numbers)
# # nums = [345, 123, 456, 678, 11, 19, 3]
# # nums.sort(reverse=True) #метод sort сортирует данные из списка 
# # print(nums)

# lst = ["Geeks", "Hello", "World", "Abc", "Bayas"]
# lst.sort()
# print(lst)

# #Tuple - картежи
# # numbers = ("Asus", "Lenovo", "Apple", "HD", "Acer")
# # print(numbers)
# # print(numbers.count('Acer'))
# # print(numbers.index('Acer'))
# # print(numbers[2])
# # print(numbers[::-1])
# # tup = (10, 3.1, "Hello", True)
# # print(tup)

# students = ["Nurbolot", "Bayastan", "Syimyk", "Beksultan", "Janysh"]
# name = input("Имя: ").title()
# if name in students:
#     print(name, "есть в списке")
# else:
#     print("К сожелению такого студента нету в списке")

# import random

# random_number = random.randint(1, 3)
# print(random_number)
# user_number = int(input("Введите число: "))
# if random_number == user_number:
#     print("Победа! Вы выиграли!")
# else:
#     print("К сожелению вы проиграли (")