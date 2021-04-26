import sys
input = sys.stdin.readline

T = int(input())

for idx in range(T):
    N = int(input())
    candidates = []
    for jdx in range(N):
        candidates.append(list(map(int, input().split())))

    candidates.sort()
    compared = candidates[0]
    count = 1

    for candidate in candidates[1:]:
        if candidate[1] < compared[1]:
            count += 1
            compared = candidate

    print(count)