#greedy
activities = [(1, 3), (2, 5), (4, 6), (6, 7)]
activities.sort(key=lambda x: x[1])

count = 0
end = 0

for start, finish in activities:
    if start >= end:
        print(start, finish)
        end = finish
        count += 1
