k, w, m = map(int, input().split())

roznica_wzrostu = w - k


if roznica_wzrostu <= 0:
    liczba_uderzen = 0
else:
    liczba_uderzen = (roznica_wzrostu + m - 1) // m

print(liczba_uderzen)
