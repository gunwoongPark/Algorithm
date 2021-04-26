TC = []

while True:
    tc = list(map(int, input().split()))
    if not bool(sum(tc)):
        break
    TC.append(tc)

for idx, tc in enumerate(TC):
    L, P, V = tc[0], tc[1], tc[2]
    div, mod = divmod(V, P)
    if mod > L:
        result = div * L + L
    else:
        result = div * L + mod

    print('Case {}:'.format(idx+1), result)