# Рассмотрим три числа a, b и c.
# Упорядочить по возрастанию. sort()
# Какое число будет стоять между двумя другими?

# Пример 1

# Ввод: 1 2 3
# Вывод: 2

value = input("Введите три числа: ") # "1 2 3"
a, b, c = map(int, value.split())

if (a <= b and a >= c) or (a >= b and a <= c):
    print(a)

elif (b <= a and b >= c) or (b >= a and b <= c):
    print(b)
    

