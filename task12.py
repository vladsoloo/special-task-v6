a = float(input("Введите значение a (1 < a < 1.5): "))


if a <= 1 or a >= 1.5:
    print("Значение a должно быть в диапазоне (1, 1.5)")
else:
    n = 2
    while True:
        number = 1 + 1/n
        if number < a:
            print(f"Первое число меньше {a}: {number} (при n = {n})")
            break
        n += 1
