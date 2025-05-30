# # Вставить разделитель разрядов в виде нижнего тире (,) и оруглить до целого числа

# x = 12345678.876567876

# print(f'{x: _.0f}') # где '_' - вид разделителя (может быть другой знак)
#                    # '.0f' - означает округлить до целого числа
#                    #  (f - float, число с плавающей точкой) 


# Выравнивание строк в поле с заданной шириной

# name = "Python"
# print(f'{name}')    # печатает текст с начала строки
# print(f'{name:->10}')    # печатает текст в поле шириной 10 символов с отступом с правого края 
# print(f'{name:-<10}')    # печатает текст в поле шириной 10 символов с отступом с левого края 
# print(f'{name:-^10}')    # печатает текст с центрированием в поле шириной 10 символов



# Красиво вывести дату или время в f-строчке

# from datetime import datetime

# now = datetime.now()
# print(f'{now:%d/%m/%Y}')       # выводим дату с разделителем '/'
# print(f'{now:%d.%m.%Y}')       # выводим дату с разделителем '.'
# print(f'{now:%H:%M:%S}')       # выводим время в формате 24 ч.
# print(f'{now:%I:%M:%p}')       # выводим время в формате 12 ч.
# print(f'{now:%Y-%m-%d_%H-%M}') # выводим дату и время

# Моментальная проверка и вывод результата

# """например есть две переменные"""
# a = 10
# b = 20
# # обычно, если мы хотим посмотреть значение, то делаем примерно так:
# print('a + b =с', a + b) # на экран выводится "a + b = 30"

# print(f'{a + b = }') # а вот так код будет короче и красивее с f-строкой 

# """можно дебажить какие нибудь  функции внутри f-строки"""
# print(f'{sorted([3, 2, 1]) = }') # передаем в f-строку функцию 'sorted()' и добавим в нее список
#                               # можно сразу увидеть результат "[1, 2, 3]"
# # если в указанных f-строках не ставить знак  '=' то на экран выведется
# # только результат, например просто 30 или [1, 2, 3] 

# """можно совмещать предыдущие фишки. Например мы хотим посмотреть, что у нас будет в 'x', после
# какой нибудь операции"""
# x = 12345.7659898
# print(f'{x = :.2f}')

# """можем управлять тем, как будет отображаться объект"""
# text = "hello"
# print(f'{text = !s}') # выводим значение нашей строки. Получим: text = hello

# print(f'{text = !r}') # выводим нашу строку непосредствено. Получим: text = 'hello', тем самым
#                       # мы видим к какому типу данных относится наша строка, если бы вместо текста
#                       # 'hello' было бы число, без наличия кавычек мы бы не поняли, что это число
#                       # относится к 'str', а не к 'int' 


"""Переопределить какой объект будет отображаться в f-строке"""

class Money:
    def __init__(self, amount, currency):
        self.amount = amount     # количество денег
        self.currency = currency # валюты

    def __format__(self, spec):
        if spec == 'symbol':  # спецификация (2-й аргумент), если нужно получить символ валюты
            symbols = {'USD': '$', 'RUB': 'P', 'EUR': 'E'}
            symbol = symbols.get(self.currency, "") # ищет символ валюты - значение ключа в словаре, если 
                                                    # такого символа нет, передаёт пустую строку
            return f'{symbol}{self.amount:.2f}' # возвращает либо символ и сумму, либо только сумму, 
                                                # и округляет сумму до 2-го знака после точки
        elif spec == 'code':  # спецификация (2-й аргумент), если нужно получить код валюты 
            return f'{self.amount:.2f} {self.currency}'
        return str(self.amount) # возвращает сумму в виде строки, если 2-й аргумент не передавался

m = Money(1999.99, "RUB")

print(f'{m:symbol}')
print(f'{m:code}')
print(f'{m}')

