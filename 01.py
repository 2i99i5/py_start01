# coding: utf-8

# PEP-8

sec = input("Введите время в секундах: ")
if sec.isdigit():  # проверка ввода
    sec = int(sec)
    hh = sec // 3600  # часы
    mm = sec % 3600 // 60  # минуты
    ss = sec % 60  # секунды
    print(f"{sec} составляет: {hh:02d}:{mm:02d}:{ss:02d}")  # :02d - 2 десятичных символа
else:
    print("Необходимо ввести число, программа завершена")
