t = int(input())

szyszki = []
for i in range(t):
    nerkowce = list(map(int, input().split()))
    n = nerkowce[0]
    rzołedzie = nerkowce[1:]
    szyszki.append(sum(rzołedzie))

for sz in szyszki:
    print(sz)
