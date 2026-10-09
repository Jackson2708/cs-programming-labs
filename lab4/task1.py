a = float(input("Введите текущую температуру:"))
b = float(input("Введите желаемую температуру:"))
if a > b:
    print("Охлаждение")
elif a < b:
    print("Нагрев")
else:
    print("Выключен")


