# n = 세로 사이즈, m = 가로 사이즈
n, m = map(int, input().split())

# 현 좌표와 바라 보고 있는 방향
x, y, d = map(int, input().split())

# 방문 정보
visited = [[0] * m for _ in range(n)]
# 현재 좌표 방문 처리
visited[x][y] = 1

# 좌표 정보
coordinates = []
for row in range(n):
    coordinates.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0] # 세로
dy = [0, 1, 0, -1] # 가로


# 위치 좌측으로 회전
def turn_left():
    global d

    d -= 1

    if d < 0:
        d = 3
    
    return d

# 초기 방문 좌표 1
result = 1
# 현재 위치 회전 가능 수
turn_count = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    is_land = coordinates[nx][ny] == 0
    is_visited = visited[nx][ny] == 1

    if is_land and not is_visited:
        # 육지, 가보지 않은 곳
        x, y = nx, ny
        visited[nx][ny] = 1
        turn_count = 0
        result += 1
        continue
    else:
        # 회전 필요함
        turn_count += 1
    
    if turn_count == 4:
        # 모든 방향 진입 불가
        
        # 뒤로 가기 좌표
        nx = x - dx[d]
        ny = y - dy[d]

        is_land = coordinates[nx][ny] == 0
        if is_land:
            # 육지라 뒤로 갈 수 있음
            x, y = nx, ny
            turn_count = 0
        else:
            # 바다라 뒤로 갈 수 없음
            break

print(result)

"""
4 4
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1
"""