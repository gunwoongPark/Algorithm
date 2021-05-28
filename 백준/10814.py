from sys import stdin

N = int(stdin.readline())

men = []
for _ in range(N):
    age, name = stdin.readline().split()
    men.append((int(age), name))

men.sort(key=lambda man: man[0])

for man in men:
    print(man[0], man[1])