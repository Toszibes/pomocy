i, k, a = map(int, input().split())
ą = 1
while i >= 0:
    if ą % 2 != 0:
        i = i - k
        ą += 1
    else:
        i = i - a
        ą += 1
if ą % 2 == 0:
    print(1)
else:
    print(0)
