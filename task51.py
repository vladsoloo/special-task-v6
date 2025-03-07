def is_palindrome(n):
    # Преобразуем число в строку
    str_n = str(n)
    # Сравниваем строку с её перевёрнутой версией
    return str_n == str_n[::-1]


number = int(input("Введите натуральное число: "))

# Проверяем, является ли число палиндромом
if is_palindrome(number):
    print(f"{number} является палиндромом.")
else:
    print(f"{number} не является палиндромом.")
