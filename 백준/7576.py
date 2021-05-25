from collections import deque

def BFS(farm, ripe, M, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = -1

    while ripe:
        count += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft()
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if farm[nx][ny] == -1:
                    continue

                if farm[nx][ny] == 0:
                    farm[nx][ny] = farm[x][y] + 1
                    ripe.append((nx, ny))

    for idx in range(N):
        for jdx in range(M):
            if farm[idx][jdx] == 0:
                return -1
    return count

if __name__ == '__main__':
    M, N = map(int, input().split())

    farm = []
    ripe = deque()

    for idx in range(N):
        row = list(map(int, input().split()))
        for jdx in range(M):
            if row[jdx] == 1:
                ripe.append((idx, jdx))
        farm.append(row)

    print(BFS(farm, ripe, M, N))