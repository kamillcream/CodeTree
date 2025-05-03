N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 순
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

x, y = N // 2, N // 2  # 중앙 좌표
dir = 0  # 시작 방향: 북쪽
res = board[x][y]

for cmd in commands:
    if cmd == 'L':
        dir = (dir + 3) % 4
    elif cmd == 'R':
        dir = (dir + 1) % 4
    elif cmd == 'F':
        nx, ny = x + dx[dir], y + dy[dir]
        if in_range(nx, ny):
            x, y = nx, ny
            res += board[x][y]

print(res)