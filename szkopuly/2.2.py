x, k = input().split()
x = int(x)
k = int(k)

if x >= 7 * k:
    print(7000 * k)
elif 2 * x >= 7 * k:
    print(3500 * k)
elif 4 * x >= 7 * k:
    print(1750 * k)
else:
    print(0)

