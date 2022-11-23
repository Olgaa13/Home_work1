# 2. Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0,2):
            print(f'При x = {x}, y = {y}, z = {z} - {not(x or y or z) == (not x) and (not y) and (not z)}')

#Еще один вариант решения, показывает только те значения предикат, при которых утверждение истинно:
# true_count = 0
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0,2):
#             true_count = not(x or y or z) == (not x) and (not y) and (not z)
#             if(true_count == True):
#                 print(f'При x = {x}, y = {y}, z = {z} - {true_count}')
# print('При всех остальных значениях X, Y, Z утверждение ложно')    
