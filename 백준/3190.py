N = int(input())
K = int(input())

apple_location = []
for _ in range(K):
    apple_location.append(tuple(map(int, input().split())))

L = int(input())

direction_info = []
custom_mapping = lambda x : (int(x[0]), x[1])
direction_info = [custom_mapping(input().split()) for _ in range(L)]

board = [[0] * N for _ in range(N)]

for location in apple_location:
    board[location[0]-1][location[1]-1] = 2

sec = 0
head = [0, 0]
tail = [0, 0]
move_queue = [(0, 0)]

# 북 0, 동: 1, 남: 2, 서: 3
d = 1
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

board[0][0] = 1

# 빈: 0, 뱀: 1, 사과: 2
while True:
    sec += 1

    head[0] += dx[d] # 행
    head[1] += dy[d]  # 열
    if head[0] < 0 or head[1] < 0:
        break

    # 벽사
    if head[0] == N or head[1] == N:
        break
    # 몸사
    if board[head[0]][head[1]] == 1:
        break

    # 사과가 있다면
    if board[head[0]][head[1]] == 2:
        board[head[0]][head[1]] = 1
        move_queue.append((head[0], head[1]))

    # 사과가 없다면
    else:
        board[head[0]][head[1]] = 1
        tail = move_queue.pop(0)
        board[tail[0]][tail[1]] = 0
        move_queue.append((head[0], head[1]))

    if len(direction_info) != 0:
        if sec == direction_info[0][0]:
            if direction_info[0][1] == "D":
                d += 1
            else:
                d -= 1
            if d == 4:
                d = 0
            elif d == -1:
                d = 3
            direction_info.pop(0)

print(sec)