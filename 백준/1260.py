from collections import deque

def DFS(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__ == '__main__':
    N, M, V = map(int, input().split())

    trunks = []
    for _ in range(M):
        trunks.append(tuple(map(int, input().split())))

    graph = [[] for _ in range(N+1)]

    for trunk in trunks:
        graph[trunk[0]].append(trunk[1])
        graph[trunk[1]].append(trunk[0])

    for idx in range(1, N+1):
        graph[idx].sort()

    visited = [False] * (N + 1)
    DFS(graph, V, visited)
    print()
    visited = [False] * (N + 1)
    BFS(graph, V, visited)