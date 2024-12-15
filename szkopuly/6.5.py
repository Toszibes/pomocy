a = input().strip()

if (a[0] == 'a' or a[0] == 'h') and (a[2] == '1' or a[2] == '8'):
    print('3')
elif (a[0] == 'a' or a[0] == 'h') or (a[2] == '1' or a[2] == '8'):
    print('5')
else:
    print(8)
