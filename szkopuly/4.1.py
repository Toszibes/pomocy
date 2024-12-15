n = int(input())
a = list(map(int, input().split()))
sumy = []
suma = 0

for number in a:
    suma += number
    sumy.append(suma)

print(" ".join(map(str, sumy)))
