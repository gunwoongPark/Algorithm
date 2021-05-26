from collections import deque
from sys import stdin

def BFS(graph, y, x):
    global count
    queue = deque()
    queue.append((x, y))

    # 상 하 좌 우 상좌, 상우, 하좌, 하우
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]

    while queue:
        x, y = queue.popleft()
        graph[y][x] = 0

        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue

            if graph[ny][nx] == 0:
                continue

            queue.append((nx, ny))

    count += 1

if __name__ == '__main__':
    result = []
    while True:
        w, h = map(int, stdin.readline().split())
        # 태스트 케이스 종료 조건
        if w == 0 and h == 0:
            break

        graph = [0] * h
        for idx in range(h):
            graph[idx] = list(map(int, stdin.readline().split()))

        count = 0
        for idx in range(h):
            for jdx in range(w):
                if graph[idx][jdx] == 1:
                    BFS(graph, idx, jdx)

        result.append(count)

    s = ""
    for answer in result:
        s += str(answer) + '\n'
    print(s)