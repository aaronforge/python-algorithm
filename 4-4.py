n, m = map(int, input().split())

# x = 세로 row 좌표, y = 가로 column 좌표
x, y, direction = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

# d = 북 0, 동 1, 남 2, 서 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 기록
d = [[0] * m for _ in range(n)]
d[x][y] = 1

def turn_left():
    global direction

    direction -= 1

    if direction < 0:
        direction = 3
    
    return direction

result = 1
turn_count = 0
while True:
    # 1. 왼쪽 방향으로 90도 회전
    turn_left()

    nx, ny = x+dx[direction], y+dy[direction]

    # 2. 앞에 안 간 칸이 존재한다면 전진
    if d[nx][ny] == 0 and data[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        result += 1
        turn_count = 0
        continue
    turn_count += 1
    # 3. 없다면(4방향 모두 돌지 않았다면) 1로 돌아감
    if turn_count == 4:
        nx, ny = x-dx[direction], y-dy[direction]
        
        # 4. 모든 방향을 다 가보았거나 움직일 수 없고 방향 유지한 채로 뒤로 이동 시 육지라면 -1 칸 이동
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            # 5. 뒤가 바다라면 멈춤
            break
        turn_count = 0

print(result)