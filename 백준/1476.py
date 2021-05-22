E, S, M = map(int, input().split())

earth, sun, moon = 0, 0, 0
year = 0

while True:
    if earth == E and sun == S and moon == M:
        break

    earth += 1
    sun += 1
    moon += 1

    if earth % 16 == 0:
        earth = 1
    if sun % 29 == 0:
        sun = 1
    if moon % 20 == 0:
        moon = 1

    year += 1

print(year)