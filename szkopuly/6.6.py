a = input()
b = 0
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
for s in samogloski:
    if s == a:
        print('tak')
        b += 1
if b == 0:
    print('nie')

