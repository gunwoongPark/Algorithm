T = int(input())

A, B, C = 300, 60, 10
push = [0,0,0]
flag = False

while T!=0:
    if T >= A:
        T -= A
        push[0] += 1
    elif T >= B:
        T -= B
        push[1] += 1
    elif T >= C:
        T -= C
        push[2] += 1
    else:
        flag = True
        break

if flag :
    print(-1)

else :
    print(push[0], push[1], push[2])