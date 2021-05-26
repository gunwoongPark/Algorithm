from collections import deque
from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**9)

def BFS(graph, y, x):


if __name__ == '__main__':
    h, w = map(int, stdin.readline().split())

    graph = [0] * h

    for idx in range(h):
        graph[idx] = list(map(int, stdin.readline().split()))

    for idx in range(h):
        for jdx in range(w):
            if graph[idx][jdx] == 2:
                BFS(graph, idx, jdx)