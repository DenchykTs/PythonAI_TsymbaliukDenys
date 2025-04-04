#
# try:
#     print(10/0)
#
# except(ArithmeticError):
#     print("Винекла арифметична помилка")
#
# except(ZeroDivisionError):
#     print("Не можливо ділити на 0")
#
# print("Програма продовжує працювати")
#
# class BuildingError(Exception):
#     def __str__(self):
#         return f"З такою кількістю матеріалів неможливо побудувати будинок."
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "Достатньо матеріалів"
#     else:
#         raise BuildingError(amount_of_material)
#
# material = 123
# check_material(material, 300)
#
# try:
#     numerator = int(input("Введіть чисельник :"))
#     denominator = int(input("Введіть знаменник: "))
#     print(numerator / denominator)
# except ZeroDivisionError:
#     print("Помилка: Ділення на 0 неможливе")
# except ValueError:
#     print("Помилка: Введенні дані не є числом")

import warnings
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)


warnings.warn("Warning, no cade here", SyntaxWarning)
try:
    warnings.warn("Warning, module not import", ImportWarning)
except Exception:
    print("Warning")

