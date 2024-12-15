f = int(input())
g = str(f // 3600) + 'g'
m = str(f % 3600 // 60) + 'm'
s = str(f % 60) + 's'
print(g, end='')
print(m, end='')
print(s, end='')
