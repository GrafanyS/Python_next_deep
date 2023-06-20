"""
Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, старые данные
из ранее созданных экземпляров сохраняются в пару списков-архивов, которые также являются свойствами экземпляра.
"""


# class Archive:
#     _instance = None
#
#     def __new__(cls, number: int, value: str):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.numbers = []
#             cls._instance.values = []
#         else:
#             cls._instance.numbers.append(cls._instance.number)
#             cls._instance.values.append(cls._instance.value)
#         return cls._instance
#
#     def __init__(self, number: int, a_string: str):
#         self.number = number
#         self.a_string = a_string
#
#     def __str__(self):
#         return f'{self.number} {self.a_string}'
#
#
# if __name__ == '__main__':
#     # a_1 = Archive(1, 'Раз')
#     # a_2 = Archive(2, 'Два')
#     a = Archive(10, 'ten')
#     b = Archive(11, 'eleven')
#     c = Archive(12, 'twelve')
#     print(a)
#     print(b)
#     print(c)
#     print(a.numbers)
#     print(a.values)
#     print(b.numbers)
#     print(b.values)
#     print(c.numbers)
#     print(c.values)


class Archive:
    '''Сохраняем данные каждого экземпляра класса в списки numbers и values.'''
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        '''Переопределили метод new для сохранения аргументов в списки.'''
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        '''Определили метод инициализации экземпляра класса.'''
        self.number = number
        self.value = value

        """
        Доработаем класс Архив из задачи 2. Добавьте методы представления 
        экземпляра для программиста и для пользователя.
        """



if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    a_2 = Archive(2, "Два")
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, "Три")
    print(f'{a_3.numbers} {a_3.values}')
    help(a_1)

    """
    class Archive:
    '''Сохраняем данные каждого экземпляра класса в списки numbers и values.'''
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        '''Переопределили метод new для сохранения аргументов в списки.'''
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        '''Определили метод инициализации экземпляра класса.'''
        self.number = number
        self.value = value

    def __repr__(self):
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        return f'Номер: {self.number}, Значение: "{self.value}"'


if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    # a_2 = Archive(2, "Два")
    # print(f'{a_1.numbers} {a_1.values}')
    # print(f'{a_2.numbers} {a_2.values}')
    # a_3 = Archive(3, "Три")
    # print(f'{a_3.numbers} {a_3.values}')
    # help(a_1)
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)
    """
