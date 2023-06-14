"""
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
●	Каждый ключевой параметр сохраните как отдельный ключ json словаря.
●	Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
●	Имя файла должно совпадать с именем декорируемой функции.
"""
import json
from typing import Callable


# def decorator(func: Callable):
#     final_dict = {}
#     with open(f'{func.__name__}.json', 'r') as f:
#         data = json.load(f)
#         final_dict.update(data)
#         json.dump(data, f, indent=2)
#
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         for i in range(len(args)):
#             data.update({i: args[i]})
#         data.update({**kwargs})
#         with open(f'{func.__name__}.json', 'w') as f_js:
#             json.dump(data, f_js, indent=2)
#
#     return wrapper
#
#
# @decorator
# def multy(a: int, b: int, *args, **kwargs) -> int:
#     return a * b
#
#
# multy(2, 3, a=2, b=3)


# import json
# from typing import Callable


def deco(func: Callable):
    with open(f'{func.__name__}.json', 'r') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # for i in range(len(args)):
        final_dict.update({str(res): args[res]})
        final_dict.update({**kwargs})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict, f, indent=2)

    return wrapper


@deco
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


multy(6, 7, temp=2, res=3, c=2, d=5)