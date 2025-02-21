def print_numbers_less_than_a(a):
    n = 1
    while True:

        current_number = 1 + 1 / n

        if current_number < a:
            print(current_number)
        else:

            break

        n += 1


a = float(input("Введите число a: "))


print_numbers_less_than_a(a)
