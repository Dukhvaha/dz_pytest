# class MathOperations:
#     def multiply(self, x, y):
#         if not isinstance(x,(int,float) and isinstance(y,(int,float))):
#             raise TypeError('Аргументы должны быть int and float')
#         return x * y
#
#     def power(self, x, y):
#         if not isinstance(y,(int,float)):
#             raise TypeError('Степень должна быть  int')
#         return x ** y
#
#     def sqrt(self, x):
#         if not isinstance(x,(int,float)):
#             raise TypeError('Аргумент должен быть int and float')
#         if x < 0:
#             raise ValueError('Отрицательное цисло не может быть')
#         return x ** 0.5
