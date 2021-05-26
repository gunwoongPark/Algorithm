from sys import setrecursionlimit
from sys import stdin
setrecursionlimit(10**9)

def DFS(graph, V, visited):
    if visited[V] == True:
        return

    visited[V] = True

    if len(graph[V]) == 0:
        return True

    for i in graph[V]:
        if not visited[i]:
            DFS(graph, i, visited)
    return True

if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (N+1)

    count = 0

    for idx in range(1, N+1):
        if DFS(graph, idx, visited):
            count += 1

    print(count)