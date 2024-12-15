a = input()
slowo = []
for i in a:
    slowo.append(i)
slowo.reverse()
b = ''.join(slowo)

if a == b:
    print('tak')
else:
    b = b.upper()
    owols = [a, b]
    c = ''.join(owols)
    print(c)
    
