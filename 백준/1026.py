from sys import stdin

N = int(input())

A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.sort()
B.sort(reverse=True)

sum = 0
for a_el, b_el in zip(A, B):
    sum += a_el * b_el

print(sum)