change = 1000-int(input())

coin_count = 0

while change >= 500:
    coin_count += 1
    change = change - 500

while change >= 100:
    coin_count += 1
    change = change - 100

while change >= 50:
    coin_count += 1
    change = change - 50

while change >= 10:
    coin_count += 1
    change = change - 10

while change >= 5:
    coin_count += 1
    change = change - 5

while change >= 1:
    coin_count += 1
    change = change - 1

print(coin_count)