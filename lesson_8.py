#Работа с файлами
# f = open('geeks.txt', 'w')
# f.write("Hello World and Geeks IT courses!")
# f.close()

# read_txt_file = open('geeks.txt', 'r')
# print(read_txt_file.read())
# read_txt_file.close()

# read_python_code_file = open('lesson_7.py', 'r', encoding='utf-8')
# print(read_python_code_file.read())
# read_python_code_file.close()

# text = 'Образовательный центр Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию.'
# about = open('about.txt', 'w', encoding='utf-8')
# about.write(text)
# about.close()

# read_text = open('about.txt', 'r', encoding='utf-8')
# print(read_text.read())
# read_text.close()

# car_text = open('car.txt', 'w', encoding='utf-8')
# car_text.write('Tesla\n')
# car_text.write('Acura\n')
# car_text.write('Zeekr\n')
# car_text.close()

# new_car_txt = open('car.txt', 'a+', encoding='utf-8')
# new_car_txt.write('Jetour\n')
# new_car_txt.close()

# with open('courses.txt', 'w', encoding='utf-8') as courses:
#     courses.write('Geeks\n')
#     courses.write('Mad Devs')

# with open('courses.txt', 'r', encoding='utf-8') as read_courses:
#     print(read_courses.read())

# with open('hello.py', 'w', encoding='utf-8') as py:
#     py.write("print('Hello World')")

# with open('lesson_8.py', 'a+', encoding='utf-8') as lesson:
#     lesson.write('name = "Nurbolot"\n')
#     lesson.write('print("name)\n')

def welcome(name:str):
    print("Здравствуйте", name)

def add(number1, number2):
    print(number1 + number2)