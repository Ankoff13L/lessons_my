

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

# # Перебирай весь список и временно присваивай переменной 'x' значение каждого элемента
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


# # Цикл для подсчёта суммы чётных чисел

# s = 0
# for num in [11, 13, 18, 24, 7, 10]: 
#     if num % 2 == 0: # Конструкция 'if' для определения чётных чисел (деление на остаток: если число
#                      # делится на 2 без остатка, значит это чётное число)
#         s += num     # Сдесь чётные числа прибавляются друг к другу: 18+24+10=52

# print(s)


# m = -1_000_000_000_000_000_000_000_000
# for num in [11, 13, 18, 24, 7, 10]:
#     if num % 2 == 0 and num > m: 
#         m = num

# print(m)
# m.__str__()



# a = [10, 23, 8, 17, 'hello', 'cat', 'dog', 45, [1, 2, 3]]

# print(len(a))
# print(len('hello'))


# for num in "раз", "два", 8, 12:
#     print("hello world")



# # for - цикл. Совершает последовательную итерацию элементоа в итерируемом объекте
# - списки
# - кортежи
# - строки
# - словари
# - файлы
# - генераторы: range()   # ("диапазон") - генерирует последовательность чисел для 
#                         # управления количеством итераций
#               enumerate()   # ("перечислить") - позволяет получить индекс и элемент одновременно





# for index, value in enumerate(["a", "b", "c"]):
#         print(index, value)



# d = {"a"= 1, "b"= 2}
# for key in d: # ключи
# for value in d.values(): # значения
# for key, value in d.items() # пары



# Для словарей можно перебирать ключи, значения или пары:
# d = {"a": 1, "b": 2}
# for key in d:                 # ключи
#     print(key)

# for value in d.values():      # значения
#     print(value)
    
# for key, value in d.items():  # пары
#     print(key, value)

# for num in range(5):
#     print(num)

# fruits = ["apple", "banana", "cherry"]
# for index,fruit in enumerate(fruits):
#     print(index,fruit)  


# m = 0
# for num in [1, 4, 13, 18, 24, 7, 10]:
#     if num % 2 == 0 and num > m:
#         m = num

# print(m)

# import add_main

# result = add_main.add(10, 5)
# print(f'Сумма: {result}')

# print(__name__)

# a = 3
# b = 4
# print(a.__add__(b))

# for s in range(3):      # Внешний цикл (s): Перебирает значения от 0 до 2 (3 итерации).
#     for k in range(2):  # Внутренний цикл (k): Для каждого значения s перебирает значения 
#                         # от 0 до 1 (2 итерации).
#         print(s, k)


# a = []
# n = int(input())           # юзер вводит нужное количество иттераций и int() преобразует текст в число
# for i in range(n):
#     a.append(int(input())) # юзер вводит числа и метод .append() добавляет их в конец списока
# print(a)                   # показывает получившийся список
# print(len(a))              # считает длину списка
# print(sum(a))              # считает сумму всех чисел списка
# print(max(a))              # показывает максимальное число в списке
# print(min(a))              # показывает минимальное число в списке



# a = []
# n = int(input())
# for a in range(n):
#     a.append(int(input()))
#     a.len()
#     a.sum()
#     a.max()
#     a.min()
# print(a)

# import random                         # модуль для генерации рандомных чисел

# a = []
# n = random.randint(1, 10)             # генерирует случайное количество иттераций в пределах от 1 до 10
# for i in range(n):
#     a.append(random.randint(3, 500))  # добавляет в список случайные числа в диапазоне от 3 до 50
# print(a)


# a = (100, 200, 300)    # кортеж
# b = [100, 200, 300]    # список

# print(a.__sizeof__())  # узнаём сколько весит кортеж
# print(b.__sizeof__())  # узнаём сколько весит список


# b = (100, 200, 300)
# c = b
# b[0] = 7
# print(b)
# print(c)


# Создаём пустой словарь и наполняем его 

# d = dict()         # создаём пустой словарь
# d[12] = 100        # добавляем пару "ключ:значение"
# d['hello'] = 20    # добавляем пару "ключ:значение"
# print(d)


# """ Создаём словарь для подсчёта количества повторения элементов в словаре """

# d = dict()                             # создаем пустой словарь
# for x in [12, 13, 14, 12, 15, 17, 18]: # перебираем список чисел для проверки ключей в словаре
#     if x in d:                         # если ключ 'x' в словаре 'd' уже находится, 
#         d[x] += 1                      # тогда в паре "ключ ('x'): значение" прибавь к значению 1
#     else:                              # иначе, если пары с таким ключем нет
#         d[x] = 1                       # создай в словаре 'd' новую пару с ключем 'x' и значением 1
# print(d)



# d = {}
# for x in [12, 13, 14, 12, 15, 17, 18]:
#     if x not in d:                         
#         d[x] = 1                      
#     else:                              
#         d[x] += 1                       
# print(d)


# d = {}
# for x in 'hello word': # перебираем по буквенно строку 'hello world'. Каждый знак это ключ для словаря
#     if x in d:         # праверяем ключи на повторы в словаре d                
#         d[x] += 1      # если такой знак (ключ) уже есть в словаре, увеличиваем его значение на 1               
#     else:              # иначе                
#         d[x] = 1       # просто добавь к ключу значениен 1            
# print(d)

# p = set()    # создаём множество 'p'
# p.add(7)     # применяя метод .add() добавляем элемент 7
# p.add(8)     # добавляем элемент 8
# p.add(153)   # добавляем элемент 153
# p.add(153)   # пытаемся добавить элемент 153, но так как он повторяется, то в колекцию не добавляеся
# print(p)


# import random

# p = set()
# for i in range(1_000_000):                # добавим в множество 1 млн. элементов
#     p.add(random.randint(1, 1_000_000))   # рандомных, от 1 до 1_000_000

# print(len(p))                             # и посчитаем количество фактически добавленных в множество чисел,
#                          # после того, как он не стал добавлять сгенерированные рандомные дубликаты



# """Добавляем в список случайные (рандомные) числа (элементы)
# сгенерированные методом .randit() из модуля random"""
# import random

# l = list()
# for i in range(1_000_000):                 # перебираем 1 млн. элементов
#     l.append(random.randint(1, 1_000_000)) # генерируем и добавляем в список 'l' случайные
#                                            # (рандомные) числа, от 1 до 1_000_000
#     sum = len(l)                           # считаем длину списка и записываем в перем. 'sum'
# print(f'В list добавлено: {sum} чисел')     # выводим количество добавленых в list 'l' чисел

# """Проверим какое количество чeтных чисел от 1 до 1_000_0000 
# было добавлено в список (сколько будет совпадений)"""
# k = 0
# for i in range(1, 1_000_000): # перебираем числа в диапазоне от 1 до 1_000_000
#     if i % 2 == 0:            # если в перем. 'i' попадает четное число
#         if i in l:            # и это число встречается в списке 'l'
#             k +=1             # добавляем в перем. 'k' единицу, т.е. считаем (счетчик) количество
# print(f'Из них четных: {k}')  # выводим количество четных чисел внесенных в список 'l'

# """Вложенный цикл (цикл в цикле) с числами"""

# for i in range(5):             # цикл перебирает числа от 0 до 5
#     for x in [8, 9, 10 , 11]:  # для каждого элемента 'i' перебирает все элементы списка 'x'
#         print(i, x)            # поочередно выводит каждый элемент 'i' со всеми элементами 'x'


# """Вложенный цикл (цикл в цикле) со строками"""

# for i in ['cat', 'dog']:
#     for x in ['fish', 'meat', 'vegetables']:
#         print(i, x)


# """Задача: Вы забыли код на своем замке. Там 3 цифры
# напишите программу, которая подберет код"""

# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             print(x, y, z)



# """Задача: Вы забыли код на своем замке. Там 3 цифры
# напишите программу, которая подберет код. Дополнительно пусть 
# укажет количество комбинаций"""

# sum = 0
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             print(x, y, z)
#             sum += 1

# print(f'Количество комбинаций: {sum}')

# """Задача: Вы забыли код на своем замке. Там 3 цифры
# напишите программу, которая подберет код. Дополнительно пусть 
# укажет количество комбинаций"""

# sum = 0
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             print(x, y, z)
#             sum += 1

# print(f'Количество комбинаций: {sum}') 



# """Задача: Вы забыли код на своем замке. Там 3 цифры: 2, 3, 5 или 7
# напишите программу, которая подберет код. Дополнительно пусть 
# укажет количество комбинаций"""

# sum = 0
# for x in [2, 3, 5, 7]:
#     for y in [2, 3, 5, 7]:
#         for z in [2, 3, 5, 7]:
#             print(x, y, z)
#             sum += 1

# print(f'Количество комбинаций: {sum}') 


# """Подобрать забытый код для старого замка из комбинаций 3-х значных цифр.
# Порядок проверки: сначала верхний треугольник, затем нижний"""

# sum = 0
# for x in [153, 315, 531, 135, 351, 531]:
#     for y in [579, 795, 957, 597, 759, 975]:
#         print(f'({x}:{y})', end="   ")
#         sum += 1
#     print()


# print(f'Количество комбинаций: {sum}')
# print()

# """Таже история только наоборот: сначала нижний треугольник, потом верхний"""

# sum = 0
# for x in [579, 795, 957, 597, 759, 975]:
#     for y in [153, 315, 531, 135, 351, 531]:
#         print(f'({x}:{y})', end="   ")
#         sum += 1
#     print()

# print(f'Количество комбинаций: {sum}')
# print()




# for x in range(10):
#     for y in range(10):
#         print(f'({x}:{y})', end="  ")
#     print()
    


# a = [3 * x for x in [13, 12, 37]]
# print(a)


# import random

# a = [x + random.randint(1, 10) for x in [10, 12, 17]]
# print(a)


# def f(n):                   # Функция 'f' получет аргумент 'n = 8'
#     a = []                  # Пустой список 'a' в который добавляются числа после выполнения цикла 'for'
#     for i in range(1, n+1): # 'for' перебирает числа (элементы) в диапазоне от 1 до 8 включительно
#         if n % i == 0:      # Если число 'n'(8) делится на число в 'i' без остатка
#             a.append(i)     # это число добавляется в список 'a'. Если есть остаток, пропускается.
#     return a                # После завершения цикла 'return' возращает созданый список 'a=[1,2,4,8]

# print(f(8)) # Функция 'print' выполняет 2 действия. Сначала вызывает функцию 'f' и передет ей аргумент '8'.
            # А после завершения работы функции печатает результат ее действия - список 'а = [1, 2, 4, 8]'





# """Напишите те числа, у которых количество делителей равно ему самому"""
# def f(n):                    # Определяем функцию 'f'- которая считает количество делителей
#     k = 0                    # которая определяет счетчик количества делителей
#     for x in range(1, n+1):  # перебирает значения делителей
#         if n % x == 0:       # проверяет условие для выявления делителей без остатка
#             k += 1           # добавляет новый делитель в общее количество делителей (счетчик)
#     return k                 # возвращает посчитанное количество делителей без остатка в 'f(s)'

# for s in range(1, 100):      # перебирает значения для аргументов для вызова функции 'f'
#     if f(s) == 6:            # проверяет условие сответсвия количества делителей числу, которое они делят
#         print(s)
# """Так как по условиям функции числа без остатка делятся только на 1 и на себя, то таких
# делителей в каждом цикле 'for s in range(1,9):' будет всегда 2. Это значит, что 'print(s)' 
# отработает когда n=1 и n=2. Т.е. мы получим числа 1 и 2"""


# """ Функция count_divisors(n) подсчитывает количество делителей числа 'n' """
# def count_divisors(n):
#     k = 0                     # Счетчик делителей
#     for x in range(1, n+1):   # Перебирает числа от 1 до  'n'
#         if n % x == 0:        # Если 'n' делится на 'x' без остатка, счетчик 'k' увеличивается на 1
#             k += 1
#     return k                  # Возвращает общее количество делителей

# for b in range(1, 10):         # Перебирает числа от 1 до 9 (вкл.). Для каждого числа проверяется: 
#     if count_divisors(b) == 2: # условие, которое означает, что число имеет ровно два делителя
#         print(b)               # если условие совпадает, перебираемое (элемент из верхней строчки
#                                # цикла 'for b in range(1,10)) число 'b' печатается. 

# """ Числа, которые имеют тотлько 2 делителя (т.е. делятся только на 1 и на себя) называют 
# простыми числами """



# """ Этаже функция (подсчитывает количества делителей числа 'n') по код по другому (из двух функций) """
# def count_divisors(n):
#     k = 0                     # Счетчик делителей
#     for x in range(1, n+1):   # Перебирает числа от 1 до  'n'
#         if divisible(n, x):   # если делится без остатка, то    
#             k += 1            # добавляет единицу в счетчик
#     return k                  # Возвращает общее количество делителей

# def divisible(n, x):          # функция проверки делителей   
#     return n % x == 0         # проверяет делится ли 'n' на 'x' без остатка и возвращает если делится
#                               # в счетчик подсчета количества делителей

# for b in range(1, 10):         # Перебирает числа от 1 до 9 (вкл.). Для каждого числа проверяется: 
#     if count_divisors(b) == 2: # условие, которое означает, что число имеет ровно два делителя
#         print(b)               # если условие совпадает, перебираемое (элемент из верхней строчки
#                                # цикла 'for b in range(1,10)) число 'b' печатается. 



# """ Функция в функции в качестве параметра """
# def turbo(x):         
#     return x*x

# def apply_to_seven(f): 
#     return f(7)

# print(apply_to_seven(turbo))


# """Теже действия, но более компактно через lambda-функцию"""
# def apply_to_seven(f):
#     return f(7)

# y = apply_to_seven(lambda x: x**2)
# print(y)

# итераторы

# myiter = iter([12, 13, 14])
# # используя метод '__next__'
# print(myiter.__next__())
# print(myiter.__next__())
# print(myiter.__next__())

# myiter = iter([12, 13, 14])
# # либо функцию 'next()', которая использует метод '__next__'
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# myiter = iter('helloworld' )
#   for x in myiter:
#     print(x)


# """ Как сложить 10-ю и 50-ю строчки (в файле в каждой строке цифра, на 10 = 10, на 50 = 50 )"""
# f = open('file.txt', 'r')
# n = 100
# for i in range(1, n+1):
#     s = f.readline()
#     if i == 10:
#         x = int(s)
#     if i == 50:
#         y = int(s)
# print(x+y)


# f = open('file.txt', 'r')   # r(read)- открыть для чтения
# g = open('output.txt', 'w') # w(write)- открыть для записи (создался новый)
# x = int(f.readline())       # читает 1-ю строку 'file.txt' и приводит в числа (число 1)
# y = int(f.readline())       # читает 2-ю строку 'file.txt' и приводит в числа (число 2)
# g.write(str(x+y))           # записывает в файл 'output' строковe. версия от "x+y" (цифра 3)


# with open('file.txt', 'r', encoding='utf-8') as f:
#     """ вот тут всякие действия с временной переменной f"""




# """Вариант № 1 импорта функции из другого модуля"""

# from имя_модуля import имя_функции  # импортируется только конкретная функция

# имя_функции() # имя_модуля перед функцией указывать не нужно

# # Этот вариант более предпочтительный, так как мы точно видим какие функции и действия с
# # кодом могут произойти. Мы контролируем код, который конкретно импортировали.


# """Вариант № 2 импорта функции из другого модуля"""

# import имя_модуля  #  импортируется весь модуль целиком
# имя_модуля.имя_функции() # перед именем функции нужно обязательно указать имя модуля.

# # Этот вариант можно применять только тогда, когда мы точно знаем весь код в импортируемом модуле.
# # При импорте всего модуля импортируются весь код и возможны различные колизии. 



# def fib(x):
#     return fib(x-1) + fib(x-2) if x > 1   else x
  
# print(fib(10))

def fib(x):
    # Базовые случаи: fib(0) = 0, fib(1) = 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    # Рекурсивный случай: fib(x) = fib(x-1) + fib(x-2)
    else:
        prev1 = fib(x - 1)  # Вычисляем предыдущее число
        prev2 = fib(x - 2)  # Вычисляем число перед предыдущим
        return prev1 + prev2  # Суммируем их

print(fib(10))  # Выведет 55