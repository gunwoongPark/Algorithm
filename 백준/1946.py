import sys
input = sys.stdin.readline

T = int(input())

for idx in range(T):
    N = int(input())
    candidates = []
    for jdx in range(N):
        candidates.append(list(map(int, input().split())))

    candidates.sort()
    rank = candidates[0][1]
    count = 1
    for candidate in candidates[1:]:
        if rank > candidate[1]:
            count += 1
            rank = candidate[1]

        if rank == 1:
            break
    print(count)
