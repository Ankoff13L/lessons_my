# num = input('Введите любое целое число: ')

# if True:
#     try:
#         num = int(input('Введите любое целое число: '))
#         print(f'Вы ввели число: {num}')

#     except ValueError:
#         print('Вы ввели неправильный формат. Попробуйте ещё раз.')


 
# if 0:
#     print('Yes')
# else:
#     print('No')
#     print('hello')

# x = 0
# while x < 10000000:
#     x += 1

# print(x)
# print('The End')

# Перебирай весь список и временно присваивай переменной 'x' значение каждого элемента
# for x in ['hello', 'wird', 17]: #  
#     # Действия которые делает цикл for
#     print(x) # в данном случае печатает значение каждой временной переменной 'x',
#              # т.е. печает все элементы списка


# # Перебирай диапазон чисел от 0 до 5 (0,1,2,3,4) и временно присваивай переменной 'x' 
# # значениие каждого элемента
# for x in range(5):
#     # Действия которые делает цикл for
#     print(x) # в данном случае печатает значение каждой временной переменной 'x'


# k = 0
# for i in range(100):
#     if i > 70:
#         k += 1
    
# print(k)


# Цикл для подсчёта суммы чётных чисел

s = 0
for num in [11, 13, 18, 24, 7, 10]: 
    if num % 2 == 0: # Конструкция 'if' для определения чётных чисел (деление на остаток: если число
                     # делится на 2 без остатка, значит это чётное число)
        s += num     # Сдесь чётные числа прибавляются друг к другу: 18+24+10=52

print(s)


