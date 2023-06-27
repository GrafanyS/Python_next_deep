"""
✔ Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
вещественное число.

✔ Обрабатывайте не числовые данные как исключения.
"""


def get_number(prompt: str) -> [int, float]:
    a_number = ''
    while True:
        try:
            a_number = input(prompt)
            return int(a_number)
        except ValueError:
            try:
                return float(a_number)
            except ValueError as e:
                print(f'Допускаются только числовые значения. : {e}')


def app():
    print(get_number('Введите целое число или число с плавающей запятой: '))
    # print(type(get_number('Введите целое число или число с плавающей запятой: ')))


if __name__ == '__main__':
    app()

"""
def num_exc():
    while True:
        num = input('Введите целое или вещественное число')
        try:
            num = int(num)
            break
        except ValueError as e:
            try:
                num = float(num)
                break
            except ValueError as e:
                print(f'Вы ввели неправильное значение: {e}\n Попробуйте снова!')

    return num


if __name__ == '__main__':
    print(type(num_exc()))
"""
