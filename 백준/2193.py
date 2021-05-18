N = int(input())

C = []
C.append(0)
C.append(1)

for idx in range(2, N+1):
    C.append(C[-2]+C[-1])

print(C[N])