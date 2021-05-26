from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)

def DFS(y, x):
    global graph
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        DFS(y-1, x)
        DFS(y+1, x)
        DFS(y, x-1)
        DFS(y, x+1)
        DFS(y-1, x-1)
        DFS(y-1, x+1)
        DFS(y+1, x-1)
        DFS(y+1, x+1)
        return True
    return False

if __name__ == '__main__':
    result = []
    while True:
        w, h = map(int, stdin.readline().split())
        # 테스트 케이스 종료 조건
        if w == 0 and h == 0:
            break

        graph = [0] * h
        for idx in range(h):
            graph[idx] = list(map(int, stdin.readline().split()))

        count = 0
        for idx in range(h):
            for jdx in range(w):
                if graph[idx][jdx] == 1:
                    if DFS( idx, jdx):
                        count += 1

        result.append(count)

    s = ""
    for answer in result:
        s += str(answer) + '\n'
    print(s)