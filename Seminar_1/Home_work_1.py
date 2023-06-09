"""
Решить задачи, которые не успели решить на семинаре.

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух
других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

from random import randint
from colorama import Fore, Style

text = ""


def triangle_check(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        print('Треугольник существует')
        if a == b == c:
            print('Треугольник равносторонний')
        elif a == b or b == c or c == a:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
    else:
        print('Такого треугольника не существует')


"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


def simple():
    i = 2
    counter = 0
    NOT_SIMPLE = 1
    MIN = 0
    MAX = 100_000
    while True:
        number = int(input(f'Введите число в диапозоне от {MIN} до {MAX}: '))
        if MIN < number < MAX:
            while i <= number - 1:
                if number % i == 0:
                    counter += 1
                i += 1
            if counter >= NOT_SIMPLE:
                print('Число составное')
            else:
                print('Число простое')
            break
        else:
            print('Недопустимое значение:')


"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать 
“больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:

from random import randint

num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""


def number_guess():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 100
    COUNT_TRY = 11
    RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
    is_win = True
    for _ in range(COUNT_TRY - 1):
        # ValueError не обрабатываю вводить только числа
        number = int(input('Введи число от 0 до 1000: '))
        if number > RAND_NUMBER:
            print('Ваше число БОЛЬШЕ загаданного')
            is_win = False
        elif number < RAND_NUMBER:
            print('Ваше число МЕНЬШЕ загаданного')
            is_win = False
        else:
            print('Вы выиграли!')
            is_win = True
            break
    if not is_win:
        print('К сожалению вы проиграли')


def run():
    text_command = """
1 - Проверить является ли треугольник равнобедренным или равносторонним
2 - Проверить число простое или составное
3 - Угадать число за 10 попыток
4 - Выход из программы
Сделайте Ваш выбор:       
"""
    while True:
        command = input(Fore.BLUE + text_command + Style.RESET_ALL)
        if command == '4':
            break

        if command == '1':
            print(Fore.GREEN + '\nПроверка треугольника:' + Style.RESET_ALL)
            a = int(input('Введи число: '))
            b = int(input('Введи число: '))
            c = int(input('Введи число: '))
            triangle_check(a, b, c)

        if command == '2':
            print(Fore.GREEN + '\nПроверить число простое или составное:' + Style.RESET_ALL)
            simple()

        if command == '3':
            print(Fore.GREEN + '\nНеобходимо угадать число за 10 попыток:' + Style.RESET_ALL)
            number_guess()


if __name__ == "__main__":
    run()
