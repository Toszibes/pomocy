a, b, c = map(int, input().split())
if a == b == c:
    print(1)
elif a ** 2 + b ** 2 == c ** 2:
    print(2)
else:
    print(0)