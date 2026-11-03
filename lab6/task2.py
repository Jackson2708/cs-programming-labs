n = int(input())
if n < 2:
    print('Не простое')
else:
    d = 2
    prime = True
    while d * d <= n and prime:
        if n % d == 0:
            prime = False
        d += 1
    if prime:
        print('Простое')
    else:
        print('Не простое')
