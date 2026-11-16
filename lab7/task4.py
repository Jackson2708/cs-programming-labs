r, c = map(int, input().split())
table = []
for i in range(r):
    table.append(list(map(int, input().split())))
row_sums = []
col_sums = [0] * c
for i in range(r):
    s = 0
    for j in range(c):
        s += table[i][j]
        col_sums[j] += table[i][j]
    row_sums.append(s)
print(f'Суммы строк: {row_sums}')
print(f'Суммы столбцов: {col_sums}')
