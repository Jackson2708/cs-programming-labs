price = float(input())
age = int(input())

if price <= 0 or age < 0 or age > 120:
    print("Ошибка")
elif age <= 5:
    print("Стоимость: 0.00 руб")
elif age <= 17:
    print(f"Стоимость: {price * 0.5:.2f} руб")
elif age <= 59:
    print(f"Стоимость: {price:.2f} руб")
else:
    print(f"Стоимость: {price * 0.7:.2f} руб")