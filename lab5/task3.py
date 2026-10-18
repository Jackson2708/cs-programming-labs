n = int(input())
negative = 0
zero = 0
positive = 0
for i in range(n):
    t = float(input())
    if t < 0:
        negative += 1
    elif t == 0:
        zero += 1
    else:
        positive += 1
print(f'Ниже нуля: {negative}')
print(f'Равны нулю: {zero}')
print(f'Выше нуля: {positive}')