number = int(input("Введите число: "))

print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")