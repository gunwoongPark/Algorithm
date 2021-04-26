S = input()

first = S[0]
count = 0
flag = False

for ch in S[1:]:
    if ch != first:
        if flag == False:
            count+=1
            flag = True

    else:
        flag = False

print(count)