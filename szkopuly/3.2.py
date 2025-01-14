a = sorted(map(int, input().split()))

if a[0] + a[1] < a[2]:
    print(0)
elif a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
    print(1)
elif a[0] == a[1] == a[2]:
    print(2)
    
