def sequence(limit):
    a = 1
    result = []
    while a < limit:
        result.append(a)
        a += 1 / (len(result) + 1)
    return result


print(sequence(1.5))
