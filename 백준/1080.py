def convertMat(idx, jdx, Aarr, Atarget):
    for target_idx, origin_idx in enumerate(range(idx, idx+3)):
        for target_jdx, origin_jdx in enumerate(range(jdx, jdx+3)):
            if Atarget[target_idx][target_jdx] == 1:
                Aarr[origin_idx][origin_jdx] = 0
            else:
                Aarr[origin_idx][origin_jdx] = 1

if __name__ == '__main__':
    N, M = map(int, input().split())

    Aarr = []
    Barr = []

    for idx in range(N):
        Aarr.append(list(map(int, list(input()))))

    for idx in range(N):
        Barr.append(list(map(int, list(input()))))

    count = 0

    for idx in range(N - 2):
        for jdx in range(M - 2):
            Atarget = [row[jdx:jdx+3] for row in Aarr[idx:idx+3]]
            Btarget = [row[jdx:jdx+3] for row in Barr[idx:idx+3]]
            if Atarget == Btarget:
                continue
            else:
                convertMat(idx, jdx, Aarr, Atarget)
                count += 1

    if Aarr == Barr:
        print(count)
    else:
        print(-1)