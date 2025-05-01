n, m = tuple(map(int, input().split()))
answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
    

def can_go(new_x, new_y):
	# 나아가려는 위치가 직사각형 안에 들어 있는지 확인하고
	# 들어있다면 아직 방문한적이 없는 곳인지 판단합니다.
    if 0 <= new_x and new_x < n and \
        0 <= new_y and new_y < m and visited[new_x][new_y] == 0:
        return True
    else:
        return False


# direction에 따라 바뀌는 (x, y)의 변화량인 dx, dy를 정의합니다.
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
curr_x, curr_y = 0, 0 # 시작은 (0, 0) 입니다.
direction = 0         # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

# 처음 시작 위치에 초기값을 적습니다.
answer[curr_x][curr_y] = 'A'
visited[curr_x][curr_y] = True

# n*m개의 알파벳을 적어야 합니다. 
for i in range(1, n * m): # i번째 문자를 어디에 적을지 결정합니다.
    while True:           # 나아갈 수 있을때까지 방향을 바꿔가며 확인해봅니다. 
        # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
        next_x, next_y = \
            curr_x + dxs[direction], curr_y + dys[direction]
        # 그 위치로 나아갈 수 있는지 확인합니다.
        if can_go(next_x, next_y):
            # 나아갈 수 있다면 위치를 갱신해주고 배열에 올바른 값을 채워넣습니다.
            curr_x, curr_y = next_x, next_y
            visited[curr_x][curr_y] = True
            answer[curr_x][curr_y] = chr((i % 26) + ord('A'))
            break
        else:
            # 나아갈 수 없다면 시계방향으로 90'를 회전하여 
			# 그 다음 방향을 확인해봐야 합니다.
            direction = (direction + 1) % 4

# 출력:
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()