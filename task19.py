def next_fraction(prev_numerator, prev_denominator, curr_numerator,
                  curr_denominator):
    """Вычисляет следующую дробь в последовательности"""
    next_numerator = prev_numerator + curr_numerator
    next_denominator = prev_denominator + curr_denominator
    return next_numerator, next_denominator


def fraction_value(numerator, denominator):
    """Вычисляет значение дроби как float"""
    return numerator / denominator


def find_close_fractions():

    prev_num, prev_denom = 1, 1  # Первая дробь: 1/1
    curr_num, curr_denom = 2, 1  # Вторая дробь: 2/1

    i = 2
    while True:

        next_num, next_denom = next_fraction(prev_num, prev_denom, curr_num,
                                             curr_denom)

        curr_val = fraction_value(curr_num, curr_denom)
        next_val = fraction_value(next_num, next_denom)

        diff = abs(curr_val - next_val)
        if diff <= 0.001:
            print(f"Найдены близкие дроби: ")
            print(f"{curr_num}/{curr_denom} ≈ {curr_val:.6f}")
            print(f"{next_num}/{next_denom} ≈ {next_val:.6f}")
            print(f"Разница: {diff:.6f}")
            break

        prev_num, prev_denom = curr_num, curr_denom
        curr_num, curr_denom = next_num, next_denom
        i += 1

        if i > 100:
            print("Превышено максимальное количество итераций")
            break


find_close_fractions()
