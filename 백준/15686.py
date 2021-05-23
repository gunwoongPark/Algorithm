from itertools import combinations

N, M = map(int, input().split())

city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

homes = []
chickens = []

for idx in range(N):
    for jdx in range(N):
        if city[idx][jdx] == 1:
            homes.append((idx+1, jdx+1))
        elif city[idx][jdx] == 2:
            chickens.append((idx+1, jdx+1))

min_dis = float('inf')
for chicken in combinations(chickens, M):
    sum = 0
    for home in homes:
        sum += min([abs(home[0] - ch[0]) + abs(home[1] - ch[1]) for ch in chicken])
    if min_dis > sum:
        min_dis = sum

print(min_dis)