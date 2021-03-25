import math

N = int(input())
candidates = list(map(int, input().split(' ')))
B, C = map(int, input().split(' '))
result = 0

for idx in range(0, len(candidates)):
    if candidates[idx] - B <=0:
        candidates[idx] = 0
    else :
        candidates[idx] = candidates[idx] - B

result += len(candidates)

for candidate in candidates :
    if candidate == 0 :
        continue
    if candidate <= C:
        result += 1
    else :
        if (candidate/C) is int :
            result += candidate/C
        else :
            result += math.ceil(candidate/C)

print(int(result))