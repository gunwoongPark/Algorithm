N = int(input())

length = list(map(int, input().split()))

city = list(map(int, input().split()))

pay = 0
oil = 0

pay = length[0] * city[0]
cheap_oil = city[0]

rest_len = sum(length) - length[0]

for bet, oil in zip(length[1:], city[1:-1]):
    if cheap_oil * bet < oil * bet:
        pay += cheap_oil * bet

    else :
        cheap_oil = oil
        pay += oil * bet

print(pay)