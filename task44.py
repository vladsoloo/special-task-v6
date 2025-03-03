def count_unique_numbers():
    numbers = set()  # Используем множество для хранения уникальных чисел
    while True:
        num = float(input("Введите число (для окончания введите 0): "))
        if num == 0:  # Проверяем конец последовательности
            break
        numbers.add(num)  # Добавляем число в множество
    print(f"Количество различных чисел: {len(numbers)}")


count_unique_numbers()
