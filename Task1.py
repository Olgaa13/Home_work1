# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.

a = int(input('Введите цифру дня недели: '))
if (a >= 1 and a <= 5):
    print('Это будний день!')
elif ((a == 6) or (a == 7)):
    print('Это выходной день!')    
else:
    print('Такого дня недели не существует!')    
