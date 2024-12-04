c = input('Na binarne czy dziesiętne? ')
z = int(input('Ile miejsc po przecinku: '))
if c == 'Binarne' or c == 'binarne':
    ę = input('Podaj liczbę dziesiętną: ')
    ą = int(float(ę))
    bą = ''
    if ą == 0:
        bą = '0'
    else:
        while ą > 0:
            bą = str(ą % 2) + bą
            ą //= 2

    y = float(ę) - int(float(ę))
    wynik = []

    for i in range(z):
        y *= 2
        if y > 1:
            wynik.append(1)
            y -= 1
        elif y < 1:
            wynik.append(0)
        else:
            wynik.append(1)
            break

    cos = ''.join(map(str, wynik))
    print(bą + '.' + cos)

if c == 'Dziesiętne' or c == 'dziesiętne' or c == 'Dziesietne' or c == 'dziesietne':
    b = input('Podaj liczbe binarną: ')
    e = b.split('.')
    if e == b or z == 0:
        print(int(b, 2))
    else:
        l1 = int(e[0], 2)
        ans = 0
        u = 2
        for d in e[1]:
            ans += int(d) / u
            u *= 2
        tmp = l1 + ans
        tmp = f"{tmp:.{z}f}"
        print(tmp)
