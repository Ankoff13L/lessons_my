

def modify(x, y):
    x += 1       # Создается новый объект (не влияет на исходный x)
    y.append(4)  # Изменяет исходный список

num = 10
numbers = [1, 2, 3]
modify(num, numbers)
print(num)     # 10 (не изменился)
print(numbers) # [1, 2, 3, 4] (изменился)
