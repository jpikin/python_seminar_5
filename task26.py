# # Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# # *Пример:*
# # A = 3; B = 5 -> 243 (3⁵)
# #     A = 2; B = 3 -> 8 




def power(x, y):
    if y == 0:  
        return 1
    elif y > 0:  
        return x * power(x, y - 1)
    else:  
        return 1 / power(x, -y)     

a, b = int(input()), int(input())
print(power(a, b))        


