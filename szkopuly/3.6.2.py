i, k, a = map(int, input().split())

if k > i % (k + a):
    print(1)
else:
    print(0)
