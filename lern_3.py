# numbers = [1, 2, 3]
# min_len = 1

# for num in numbers:
#     if num == min_len:
#         print(f'num: {num}')
#         break
# else:
#     print(f'Finish...')


# numbers = [1, 2, 3]
# min_len = 1

# for num in numbers:
#     if num == min_len:
#         print(f'num: {num}')
#         # break
# else:
#     print(f'Finish...')


# numbers = 0

# try:
#     10 / numbers
# except ZeroDivisionError:
#     print("Oops..")
# else:
#     print(f'{numbers = }')
# finally:
#     print("Program finished..")

my_tuple = (1, 2, [3, 4])  # Кортеж с числом и списком
print(my_tuple)  # (1, 2, [3, 4])

# Попытка изменить сам кортеж вызовет ошибку:
# my_tuple[0] = 10  # ❌ Ошибка: кортеж неизменяем!

# Но мы можем менять список внутри кортежа:
my_tuple[2].append(5)  # ✅ Работает!
print(my_tuple)  # (1, 2, [3, 4, 5])


