n = int(input())
odd = 0
for r in range(n):
    value = 1
    for k in range(r + 1):
        if k > 0:
            print(' ', end='')
        print(value, end='')
        if value % 2 == 1:
            odd += 1
        value = value * (r - k) // (k + 1)
    print()
print(f'Нечетных элементов: {odd}')