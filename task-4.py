value = int(input("Введите сумму продажи: "))

discount = 0

if value > 0:
    if value > 25000:
        discount = 0.3
    elif value > 15000:
        discount = 0.2
    elif value > 5000:
        discount = 0.12
    else:
        discount = 0.05

    discount_value = value * discount
    total_value = value - discount_value

    print(f"Скидка: {discount_value}")
    print(f"Сумма с учетом скидки: {total_value}")

else:
    print("Некорректная сумма")