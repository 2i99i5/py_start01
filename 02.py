# coding: utf-8

# PEP-8

num = input("Введите число: ")
if num.isdigit():  # проверка ввода
    sum = int(num) + int(num * 2) + int(num * 3)
    print(f"Cумма равна {sum}")
else:
	print("Необходимо ввести число, программа завершена")
