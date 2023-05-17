"""
Задание №1
 Установили Python и IDE для работы
"""

"""
Задание №2
Работаем в командной строке (терминале ОС)
Создайте каталог для проекта first_project и разверните
виртуальное окружение Python в папке venv внутри каталога
Создайте третий каталог проекта project_new и разверните
виртуальное окружение Python в папке venv_new внутри каталога
Для каждого проекта последовательно активируйте
и деактивируйте виртуальное окружение
"""


# year = int(input(" Ввести год"))
#
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     print("Обычный")
#
# else:
#     print("Високосный")

# factor = 2
# number = 2
# while number < 10:
#     if factor <= 10:
#         print(f"{number}x{factor} = {number * factor}")
#         factor += 1
#     else:
#         print(" ")
#         factor = 2
#         number += 1
#         continue

rows = int(input("Задайте колличество рядов в ёлке: "))
count = 1
step = " "
step2 = 1
star = "*"
print(step)
while rows > 0:
    three = step * (rows - count) + star * step2
    print(three)
    rows -= 1
    step2 += 2


