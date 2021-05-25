import sys

sys.setrecursionlimit(10000)

def DFS(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        return True
    return False

result = []
T = int(input())
for _ in range (T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        loc = tuple(map(int, input().split()))
        graph[loc[1]][loc[0]] = 1

    count = 0
    for idx in range(N):
        for jdx in range(M):
            if DFS(idx, jdx) == True:
                count += 1

    result.append(count)

for answer in result:
    print(answer)