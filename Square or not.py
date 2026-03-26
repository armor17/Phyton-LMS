x = int(input())
if x ** 0.5 % 1 == 0:
    condition = True
else:
    condition = False
if condition == True:
    print('Квадрат')
else:
    print('Не квадрат')
