N = int(input())

people = []
for _ in range(N):
    people.append(tuple(map(int, input().split())))

result = []

for person in people:
    rank = 1
    for idx in range(len(people)):
        if person[0] < people[idx][0] and person[1] < people[idx][1]:
            rank += 1
    result.append(rank)

for el in result:
    print(el, end=" ")