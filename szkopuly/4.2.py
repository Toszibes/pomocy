n = int(input())
dzielniki = [1, n]
if n % 2 == 0:
    dzielniki.append(int(n/2))

for i in range(2, int((n/2)+1)):
    if n % i == 0:
        dzielniki.append(i)
dzielniki = sorted(dzielniki)
ę = 0
for d in dzielniki[:-1]:
    if dzielniki[ę] == dzielniki[ę+1]:
        ę += 1
    else:
        print(d)
        ę += 1
print(n)
