#freq map using set+dict
arr = [1, 2, 2, 3, 3, 3]

count = {}

for i in arr:
    count[i] = count.get(i, 0) + 1

print(count)
