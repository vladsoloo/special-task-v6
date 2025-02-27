def count_min_digit(n):

    num_str = str(n)
    min_digit = min(num_str)

    return num_str.count(min_digit)


examples = [
    102200,
    40330,
    10345,
    999999,
    12345
]

for number in examples:
    count = count_min_digit(number)
    print(f"Число: {number}")
    print(f"Количество встреч минимальной цифры: {count}\n")
