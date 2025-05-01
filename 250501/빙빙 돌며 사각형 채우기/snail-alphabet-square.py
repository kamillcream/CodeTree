n, m = map(int, input().split())

# Please write your code here.
def fill_snail(n, m):
    board = [['' for _ in range(m)] for _ in range(n)]
    
    dx = [0, 1, 0, -1]  # → ↓ ← ↑
    dy = [1, 0, -1, 0]
    
    x, y, d = 0, 0, 0
    ch = ord('A')

    for _ in range(n * m):
        board[x][y] = chr(ch)
        ch += 1
        if ch > ord('Z'):
            ch = ord('A')

        nx, ny = x + dx[d], y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '':
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]

    for row in board:
        print(' '.join(row))

# 예시 실행
fill_snail(4, 4)