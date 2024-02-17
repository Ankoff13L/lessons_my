# names = ["Христофор", "Адемар", "Тэя", "Стефания", "Архип"]
# names_starts_a = []

# for name in names:
#     if name.startswith("А"):
#         names_starts_a.append(name)

# print(names_starts_a)


names = ["Христофор", "Адемар", "Тэя", "Стефания", "Архип"]
names_starts_a = [name for name in names if name.startswith("А")]

print(names_starts_a)


