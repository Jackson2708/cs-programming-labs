numbers = list(map(int, input().split()))
target = int(input())
indexes = [i for i, x in enumerate(numbers, 0) if x == target]
print(f'Индексы: {indexes}')
