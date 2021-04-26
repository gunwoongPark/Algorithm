def convertMat(idx, jdx, Aarr):
    for i in range(idx, idx + 3):
        for j in range(jdx, jdx + 3):
            if bool(Aarr[i][j]):
                Aarr[i][j] = 0
            else:
                Aarr[i][j] = 1

if __name__ == '__main__':
    N, M = map(int, input().split())

    Aarr = []
    Barr = []

    for idx in range(N):
        Aarr.append(list(map(int, list(input()))))

    for idx in range(N):
        Barr.append(list(map(int, list(input()))))

    count = 0

    for idx in range(N-2):
        for jdx in range(M-2):
            if Aarr[idx][jdx] != Barr[idx][jdx]:
                count += 1
                convertMat(idx, jdx, Aarr)

    if Aarr != Barr:
        print(-1)
    else:
        print(count)