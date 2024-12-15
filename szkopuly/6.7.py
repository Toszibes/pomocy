a = int(input())
b = list(map(int, input().split()))
ą = 0

for i in b:
    if 100 > i >= 10:
        ą += i
print(ą)
