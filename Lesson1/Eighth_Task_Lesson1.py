a = float(input("Введи перше число: "))
b = float(input("Введи друге число: "))

operation = input("Введи дію (+, -, *, /): ")

if operation == "+":
    print("Результат:", a + b)

elif operation == "-":
    print("Результат:", a - b)

elif operation == "*":
    print("Результат:", a * b)

elif operation == "/":
    if b == 0:
        print("Помилка: ділення на нуль!")
    else:
        print("Результат:", a / b)