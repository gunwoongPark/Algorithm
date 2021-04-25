N = int(input())

ropes = []

for idx in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

weight = ropes[0]
select = []
for idx in range(len(ropes)):
    select.append(ropes[idx])
    if weight > select[-1] * len(select) :
        continue
    else :
        weight = select[-1] * len(select)

print(weight)