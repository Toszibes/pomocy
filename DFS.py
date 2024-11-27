price = float(input('podaj cene: '))
cash = float(input('ile masz kasy: '))
zlotowki = [5, 2, 1]
grosze = [50, 20, 10, 5, 2, 1]
reszta = cash - price
a = int(reszta)
b = reszta - a
    
if price - cash <= 0:
    ą = 0
    while a >= 1:
        if zlotowki[ą] <= a:
            print(zlotowki[ą])
            a = a - zlotowki[ą]
        else:
            ą += 1
    ę = 0
    while b > 0:
        if grosze[ę] <= b:
            print(grosze[ę])
            b = b - zlotowki[ę]
        else:
            ę += 1
else:
    print('biedak')
  
#print(a, b)
