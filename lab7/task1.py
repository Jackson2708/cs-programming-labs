stock = list(map(int, input().split()))
fixed = stock.copy()
for i in range(len(fixed)):
    if fixed[i] < 0:
        fixed[i] = 0
print(f'Исходные остатки: {stock}')
print(f'Исправленные остатки: {fixed}')
