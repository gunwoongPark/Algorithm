from sys import stdin

N = int(input())

dots = [0] * N
for idx in range(N):
    dots[idx] = tuple(map(int, stdin.readline().split()))

dots.sort(key=lambda dot: (dot[1], dot[0]))

for dot in dots:
    print(dot[0], dot[1])