# Циклы for и while
#  print(1)
#  print(2)
# print(3)
# print(4)
# print(5)
# # # # # for number in range(1001):
# # # # #     print(number)

# # # # for num in range(10, 21, 2): #в циклах с использованием функции range, можно указывать начало, конец и шаг
# # # #     print(num) #выводим временную переменную num 

numbers = [] #создаем пустой список numbers
for i in range(1, 100, 2): #создаем цикл for, с использованием range
    numbers.append(i) #с каждом циклом (повтором) добавляем числа в список
print(numbers) #Выводим результат(список)

# # # names = ["Bayastan", "Nurbolot", "Janysh", "Beka", "Islam"]
# # # for name in names:
# # #     print("Привет", name)

# # nums = [101, 3, 441, 1002, 4, 5, 13, 321, 777, 888, 907]
# # for num in nums:
# #     if num % 2 ==0:
# #         print(num, "четный")
# #     else:
# #         print(num, "нечетный")

# #Цикл while
# num1 = 10
# num2 = 20
# while num2 > num1:
#     num1 += 1
#     print(num1)

# n = 0
# while True:
#     n += 1
#     print(n, "Hello Geeks")
# #     if n == 10000:
# #         print("STOP")
# #         break
#     if n == 10000:
#       print("Hello")
#       continue
