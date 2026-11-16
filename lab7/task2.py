numbers = list(map(int, input().split()))
squares = [x * x for x in numbers if x > 0 and x % 2 == 1]
print(f'Квадраты: {squares}')
