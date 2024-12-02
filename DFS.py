
price = float(input('podaj cene: '))
cash = float(input('ile masz kasy: '))
zlotowki = [5, 2, 1]
grosze = [0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
a = int(cash - price)
b = (cash - price) - a
b = round(b, 2)
odp = []

if price - cash <= 0:
    ą = 0
    while a >= 1:
        if zlotowki[ą] <= a:
            odp.append(zlotowki[ą])
            a = a - zlotowki[ą]
        else:
            ą += 1
    ę = 0
    while b > 0:
        if grosze[ę] <= b:
            odp.append(grosze[ę])
            b = round(b - grosze[ę], 2)
        else:
            ę += 1
for o in odp:
    print(o)