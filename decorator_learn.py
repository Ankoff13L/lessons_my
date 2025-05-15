

# def summ(a, b):
#     return a + b

# def logger(func):                          # функция 'logger()' получает функцию 'summ()'
#     def wrapper(a, b):                     # 'wrapper()' захватывает аргументы (2 и 3) из 'logger(summ)'
#         print(f'{func.__name__} started')  # 'wrapper()' печатает имя обёрнутой функции 'summ()' + started
#         result = func(a, b)  # 'func()' получает (2,3) и передает их в 'summ(2,3)' и получает result=5 (return 2+3) 
#         print(f'{func.__name__} finished') # 'wrapper()' печатает имя обёрнутой функции 'summ()' + finished
#         return result                      # 'wrapper()' result = 5
#     return wrapper                         # 'wrapper()' возращает результат (5) в 'logger()'

# if __name__ == '__main__':
#     function = logger(summ)  # вызываем функцию 'logger()' и передаём в неё функцию 'summ'
#     print(function(2, 3))    # 1) передаём в 'logger()' аргументы '2' и '3'
#                              # 2) печатает результат 'function()', полученный из 'logger()'



# def summ(a, b):
#     return a + b

# def logger(func):                          # функция 'logger()' получает функцию 'summ()'
#     def wrapper(a, b):                     # 'wrapper()' получает аргументы (2 и 3) из 'print(summ(2, 3))'
#         print(f'{func.__name__} started')  # 'wrapper()' печатает имя обёрнутой функции 'summ()' + started
#         result = func(a, b)  # 'func()', являясь по сути 'summ(a, b)' выполняет код и записывает в result = 5
#         print(f'{func.__name__} finished') # 'wrapper()' печатает имя обёрнутой функции 'summ()' + finished
#         return result                      # result возвращает в 'wrapper' сумму равную 5
#     return wrapper                         # 'wrapper()' возращает результат (5) в 'logger()'

# if __name__ == '__main__':
#     # function = logger(summ)  
#     # print(function(2, 3))    
                           
#     """Упрощение 1. Заменим две предудущие строки кода на одну"""
#     # print(logger(summ)(2,3)) # мы вызываем 'logger()' и передаем в него функцию 'summ' (как объект)
#     # Функция 'logger()' возвращает нам обёртку 'wrapper", и уже потом передаём в 'wrapper'
#     # аргументы '2 и 3' и с ними вызываем функйию.

#     """Упрощение 2. Заменим предыдущую строчку на более читабельный код"""
    
#     summ = logger(summ)
#     # 1. Мы вызвали функцию 'logger()' и передали в неё функцию 'summ' и записали это в новую 
#     # переменную 'summ'.
#     # 2. 'logger()' вернул нам обёртку 'wrapper' и теперь 'summ' это уже по сути 'wrapper'
#     print(summ(2, 3)) # данная строка читается и произносится как "summ от 2 и 3"
#     # 3. После этого в обёртку передали аргументы '2 и 3'
#     # 4. Получив аргументы, 'wrapper' начал работать и передал их в функцию 'func()', которая по свой 
#     # сути является аватаром функции 'summ(a, b)'. Функция 'summ (2, 3)' отработала свой код (2+3=5) и 
#     # полученный результат 5 записала в переменную 'result', которая через 'return' вернула  в 'wripper'. 
#     # 'wripper' отработав свою функцию  вернул '5' и свои строк 'summ started' и 'sum finished' 
#     # на печать в функцию 'print()'


# """Код примера без комментариев, в конечной обработке выглядет так"""

# def summ(a, b):
#     return a + b

# def logger(func):                          
#     def wrapper(a, b):                     
#         print(f'{func.__name__} started')  
#         result = func(a, b)  
#         print(f'{func.__name__} finished') 
#         return result                      
#     return wrapper                         

# if __name__ == '__main__':
#     summ = logger(summ)
#     print(summ(2, 3))


# """Код примера с правильно написанным декораторм"""

# def logger(func):                          
#     def wrapper(*args): # обычно ставят'*args', так как он принимает любое кол. позиционных аргументов
#         print(f'{func.__name__} started')  
#         result = func(*args)  
#         print(f'{func.__name__} finished') 
#         return result                      
#     return wrapper                         

# @logger          # синтаксический сахар
# def summ(a, b):  # в этот момент summ=wrapper
#     return a + b

# if __name__ == '__main__':
#     # summ = logger(summ) - эта строчка уже не нужна, '@logger' её заменяет
#     print(summ(2, 3))

# """Пример"""

# from datetime import datetime

# def timeit(func):
#     def wrapper(*arks, **kwargs):
#         start = datetime.now()
#         result = func(*arks, **kwargs)
#         print(datetime.now() - start)
#         return result 
#     return wrapper

# @timeit
# def one(a):
#     # start = datetime.now()
#     n = []
#     for i in range(a):
#         if i % 2 == 0:
#             n.append(i)
#     # print(datetime.now() - start)
#     return n

# @timeit
# def two(a):
#     # start = datetime.now()
#     n = [x for x in range(a) if x % 2 == 0]
#     # print(datetime.now() - start)
#     return n

# n1 = one(100_000)
# n2 = two(100_000)

# print(n1)
# print(n2)


# from datetime import datetime

# def logger(func):
#     def wratter(*arks, **kwarks):
#         start = datetime.now()
#         result = func(*arks, **kwarks)
#         print(datetime.now() - start)
#     return wratter    

# @logger
# def sn_1(r):
#     m = []
#     for i in range(r):
#         if i % 2 == 0:
#             m.append(i)
#     return m

# @logger
# def sn_2(r):
#     m = [x for x in range(r) if x % 2 == 0]
#     return m

# sn_1 = sn_1(100_000)
# sn_2 = sn_2(100_000)

# print(sn_1())
# print(sn_2())


# из видео: Декоратор Python/Всё что нужно знать на собесе

def deco_2(func):
        def wrapper(*args, **kwargs):       # 1 выполняется этот код
            print("deco_2 before")          # 1 выполняется этот код
            result = func(*args, **kwargs)  # 2 выполняется этот код
            print("deco_2 after")           # 4 выполняется этот код
            return result

        return wrapper


def deco(func):
        def wrapper(*args, **kwargs):
            print("deco before")            # 3 выполняется этот код
            result = func(*args, **kwargs)  # 3 выполняется этот код
            print("deco after")             # 3 выполняется этот код
            return result                   # 3 выполняется этот код

        return wrapper

@deco                 # заменяет код 'summator = deco(summator)'
def summator(a, b):
    return a + b

@deco_2
@deco                 # заменяет код 'square = deco(square)'
def square(a):
    print('functional calling')
    return a * a

print(square(1))

# Сначала выполнится наружная функция 'deco_2'