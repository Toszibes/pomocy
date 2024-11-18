x = input('netto czy brutto?\n')
if x not in ('brutto', 'Brutto', 'BRUTTO'):
    print('liczysz brutto grzybie')
y = input('chcesz ppk? \n')
if y.lower() != 'tak':
    print('chcesz ppk \n')
    

zaropek = float(input('ile zarabiasz:\n'))

se = zaropek * 0.0976
sr = zaropek * 0.015
sc = zaropek * 0.0245
zd = (zaropek - (se + sr + sc)) * 0.09
ppk = zaropek * 0.015
kup = 250
zzp = ((zaropek - se - sr - sc + ppk - kup) * 0.12) - 300
netto = zaropek - se - sr - sc - zd - zzp

print('składka emerytalna: ', round(se, 2), '\n')
print('składka rentowa: ', round(sr, 2), '\n')
print('składka chorobowa: ', round(sc, 2), '\n')
print('ubezpieczenie zdrowotne: ', round(zd, 2), '\n')
print('zaliczka za podatek: ', round(zzp, 2), '\n', '\n')
print('netto: ', round(netto, 2))
