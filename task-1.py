p = int(input("Введите начальную сумму: ")) # str
r = int(input("Введите процент по вкладу: ")) # str
t = int(input("Введите количество лет: ")) # str

sum = (p * r * t) / 100

print(f"Начальная сумма вклада: {p}")
print(f"Процент по вкладу: {r}")
print(f"Количество лет: {t}")
print(f"Начисленные проценты: {sum}")