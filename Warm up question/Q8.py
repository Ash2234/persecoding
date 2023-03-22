sweets = [10, 10, 10, 10, 10]
for i in range(5):
    passed_on = int(input())
    next_index = (i + 1) % 5
    sweets[next_index] += passed_on
    sweets[i] -= passed_on

max_sweets = max(sweets)
print(max_sweets)
