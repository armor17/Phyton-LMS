x = int(input())
y = x + (x % 2 == 0) * 2 + (x % 2 != 0) * 1
print(y)
