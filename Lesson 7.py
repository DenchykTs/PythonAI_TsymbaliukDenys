# import random
# my_list = []
#
# for i in range(10):
#     my_list.append(random.randint(-10, 10))
#
# print(my_list)
# print("-"*20)
#
# iterator = iter(my_list)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# iterator = iter(my_list)
# for elem in iterator:
#     print(elem)
#
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
# counter = Counter(5)
# for elem in counter:
#     print(elem)
#
# print('-'*30)
# counter = Counter(5)
# print(counter.__next__())
# print(counter.__next__())
# print(next(counter))
#
# # генератор списку
# list_power_2 = [i ** 2 for i in range(1, 20, 1)]
# print(list_power_2)
from multiprocessing.pool import worker


# "генератори в Пайтон - це функція, що повертає ітератор, які під час ітерації генерує послідовність значень."
#
# def raise_to_the_degrees(number, max_degrees):
#     i = 0
#     # for _ in range(max_degrees):
#     while True:
#         result = number ** i
#         yield number ** i
#         # i += 1
#         if result > 100**20:
#             return
#         i += 1
#
#
#
# res = raise_to_the_degrees(2, 500)
# print(res)
#
# for elem in res:
#     print(elem)

class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"I will help you with your {self.work}. After I will help you with {work}"

helper = Helper("homework")
print(helper('cleaning'))
