count = 0
total = 0
line = input()
while line != 'stop':
    count += 1
    total += int(line)
    line = input()
if count == 0:
    print('Нет покупок')
else:
    print(f'Покупок: {count}')
    print(f'Общая стоимость: {total} руб')
    print(f'Средняя стоимость: {total / count:.2f} руб')