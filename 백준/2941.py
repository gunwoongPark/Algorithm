voca = input()

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

while len(voca):
    if voca[0:2] in croa:
        count += 1
        voca = voca[2:]
    elif voca[0:3] in croa:
        count += 1
        voca = voca[3:]
    else:
        count += 1
        voca = voca[1:]

print(count)