g = input()
h = input().split()
awers = h.count('0')
rewers = h.count('1')
if awers < rewers:
    print(awers)
else:
    print(rewers)
