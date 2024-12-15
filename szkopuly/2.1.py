n = int(input().strip())
arr = list(map(int, input().strip().split()))

min_value = 0
max_value = 0

max_value = max(arr)
min_value = min(arr)

print(max_value - min_value)
