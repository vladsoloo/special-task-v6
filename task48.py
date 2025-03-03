def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def count_of_digits(n):
    return len(str(n))


def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product


def check_conditions(n, k, b, x, y, a, n_div):
    results = {}

    # а) Сумма его цифр больше k, а само число четное
    results['a'] = (sum_of_digits(n) > k) and (n % 2 == 0)

    # б) Количество его цифр есть четное число, а само число не превышает b
    results['b'] = (count_of_digits(n) % 2 == 0) and (n <= b)

    # в) Оно начинается цифрой x и заканчивается цифрой y
    results['c'] = (str(n).startswith(str(x))) and (str(n).endswith(str(y)))

    # г) Произведение его цифр меньше a, а само число делится на b
    results['d'] = (product_of_digits(n) < a) and (n % b == 0)

    # д) Сумма его цифр больше m, а само число делится на n
    results['e'] = (sum_of_digits(n) > m) and (n % n_div == 0)

    return results


n = 1234
k = 8
b = 2000
x = 1
y = 4
a = 50
m = 10
n_div = 2

conditions_check = check_conditions(n, k, b, x, y, a, n_div)
for key, value in conditions_check.items():
    print(f"Условие {key}: {'Выполняется' if value else 'Не выполняется'}")
