while True:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    print(f"Сумма чисел: {num1 + num2}")

    accept_exit = input("Нажмите Y или y для завершения программы:")

    if accept_exit.lower() == "y": break