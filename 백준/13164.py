N, K = map(int, input().split(' '))
children = list(map(int, input().split(' ')))

diff = []

for idx in range(1, len(children)):
    diff.append(children[idx] - children[idx-1])

diff.sort()

result = 0

for idx in range(0, N-K):
    result += diff[idx]

print(result)
