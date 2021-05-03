N, L = input().split()
N, L = int(N), int(L)

leaky_pipe = list(map(int, input().split()))
leaky_pipe.sort()

last_place = 0
count = 0

for pipe in leaky_pipe:
    if last_place >= pipe:
        continue
    start = pipe - 0.5
    end = start + L
    last_place = end
    count += 1

print(count)