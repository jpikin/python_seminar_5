#  Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:
# 2 2 -> 4 


def sum(a,b):
    if b > 0: return sum(a+1,b-1)
    else: return a

a, b = int(input()), int(input())
print(sum(a,b))


# def sum(a,b): return sum(a+1,b-1) if b > 0 else a
# print(sum(int(input()),int(input())))