def count_max_digit(n):

    num_str = str(n)

    max_digit = max(num_str)
    count = num_str.count(max_digit)

    return count


examples = [
    132233,     # 3 встречи максимальной цифры
    46336,      # 2 встречи максимальной цифры
    12345,      # 1 встреча максимальной цифры
    999999,     # все цифры максимальные
    12345       # повторный пример для проверки
]

for number in examples:
    count = count_max_digit(number)
    print(f"Число: {number}")
    print(f"Количество встреч максимальной цифры: {count}\n")
