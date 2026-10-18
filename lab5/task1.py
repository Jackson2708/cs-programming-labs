a = int(input())
b = int(input())
total = 0
product = 1
for i in range(a, b + 1):
    total += i
    product *= i
print(f'Сумма: {total}')
print(f'Произведение: {product}')