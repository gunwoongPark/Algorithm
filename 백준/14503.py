def rotate():
    global d
    d -= 1
    if d == -1:
        d = 3

if __name__ == '__main__':
    N, M = map(int, input().split())

    row, column, d = map(int, input().split())

    # room = [[0] * M for _ in range(N)]
    room = []
    for idx in range(N):
        room.append(list(map(int, input().split())))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    count = 0

    # 현재 위치 청소
    room[row][column] = 2
    count += 1

    turn_count = 0

    while True:
        # 왼쪽 방향 돌기
        rotate()
        turn_count += 1

        if room[row + dy[d]][column + dx[d]] == 1 or room[row+dy[d]][column+dx[d]] == 2:
            if turn_count == 4:
                if room[row - dy[d]][column - dx[d]] == 1:
                    break
                else:
                    row -= dy[d]
                    column -= dx[d]
                    turn_count = 0
            else:
                continue

        else:
            count += 1
            row += dy[d]
            column += dx[d]
            room[row][column] = 2
            turn_count = 0
            continue

    print(count)