a, b = map(int, input().split())

ą = [a + b, a - b, a * b]
ą = set(ą)

if len(ą) == 3:
    if max(ą) == a + b:
        print(f"{a}+{b}={a + b}")
    elif max(ą) == a - b:
        print(f"{a}-({b})={a - b}")
    elif max(ą) == a * b:
        print(f"{a}*{b}={a * b}")
else:
    print("NIE")
