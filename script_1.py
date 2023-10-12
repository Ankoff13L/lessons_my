# print(f"__name__ script_1.py is {__name__}")

# if __name__ == '__main__':
#     print(f"Я работаю как независимая программа с именем {__name__}")
# else:
#     print(f"Я работаю как импортированный модуль с именем {__name__}")

def say_hello(name=""):
    print(f"Hello {name}")


def print_age(age=20):
    print(f"Age {age}")


def main():
    name = input("Enter your name please: ")
    say_hello(name=name.title())
    print_age(age=30)
    print(f"Я работаю как независимая программа с именем {__name__}")


if __name__ == '__main__':
    main()
# else:
#     print(f"Я работаю как импортированный модуль с именем {__name__}")


# name = input("Enter your name please: ")
# say_hello(name=name.title())
# print_age(age=30)
# print(f"Я работаю как независимая программа с именем {__name__}")
