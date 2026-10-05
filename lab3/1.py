num = input()
cat = num[:3]
year = num[4:8]
cif = num[-4:]
rev = num[::-1]
print(f'Категория: {cat}')
print(f'Год: {year}')
print(f'Номер: {cif}')
print(f'Обратный номер: {rev}')
