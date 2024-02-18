# names = ["Христофор", "Адемар", "Тэя", "Стефания", "Архип"]
# names_starts_a = []

# for name in names:
#     if name.startswith("А"):
#         names_starts_a.append(name)

# print(names_starts_a)


# names = ["Христофор", "Адемар","Тэя", "Стефания", "Архип"]
# names_starts_a = filter(lambda name: name.startswith("А"), names)
# print(names_starts_a)
# """ В таком виде имена не напечатеся, будет напечатано "<filter object at 0x1033fa380>" - это сам итератор.
# Нам нужно привести его значение к какому-то виду (список, кортеж), например укажем кортеж"""
# print(tuple(names_starts_a))


# numbers = [1, 200, 300]
# print(numbers)

# numbers = numbers[::-1]
# print(numbers)

# name = "Василий"
# if name == "Алексей" or name == "Петр" or name == "Христофор":
#     print(name)


# name = "Василий"
# if name in ("Алексей", "Петр", "Христофор"):
#     print(name)


# a = b = c = d = e = None
# a = b = c = d = e = True
# if a and b and c and d and e:
#     print("Any True")



# a = b = c = d = e = None
# a = b = c = d = e = True
# if any((a, b, c, d, e)): print("Any True")


# print(any([1, 0, 3, 0]))
# print(any([False, True, False]))
# print(any([False, False, False]))


# class User:
#     def __init__(self, group: str):
#         self.group = group

# user = User(group="admin")

# if user.group == "admin":
#     process_admin_request(user, request)
# elif user.group == "manager":
#     process_manager_request(user, request)
# elif user.group == "client":
#     process_client_request(user, request)



# class User:
#     def __init__(self, group: str):
#         self.group = group

# user = User(group="admin")

# group_to_process_metod = [
#     "admin": process_admin_request,
#     "manager": process_manager_request,
#     "client": process_client_request,
# ]
# group_to_process_metod[user.group](user, request)








