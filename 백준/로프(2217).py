N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse=True)

weight, last, count = ropes[0], ropes[0], 1

for rope in ropes[1:]:
    last, count = rope, count+1
    next_weight = last * count
    if weight <= next_weight:
        weight = next_weight

print(weight)