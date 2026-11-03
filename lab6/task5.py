n = int(input())
if n < 1 or n > 10:
    print('Ошибка')
else:
    for i in range(n):
        for j in range(n):
            if j > 0:
                print(' ', end='')
            if i > j:
                print(i - j, end='')
            else:
                print(j - i, end='')
        print()
