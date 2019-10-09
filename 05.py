# coding: utf-8

# PEP-8

a = input("Результат пробежки в первый день: ")
b = input("Требуемый общий результат: ")

if a.isdigit() and b.isdigit():  # проверка ввода
    count = 1  # кол-во дней
    a = int(a)
    b = int(b)
    while a < b:
        a = a * 1.1
        count += 1
    print(f"На {count} день спортсмен пробежал более {b}")
else:
    print("Необходимо ввести числа, программа завершена")
