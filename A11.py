# 보드 정보 = n * n
n = int(input())
coordinates = [[0] * (n + 1) for _ in range(n + 1)]

# 사과 수
k = int(input())

# 사과가 있는 좌표 정보
for _ in range(k):
    x, y = map(int, input().split())
    coordinates[x][y] = 1

# 방향 전환 횟수
l = int(input())

# 방향 전환 정보
directions: list[tuple[int, str]] = []
for _ in range(l):
    time, direction = input().split()
    directions.append((int(time), direction))

# 전환 좌표 방향 정보(초기값 동 부터, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 좌표
x, y = 1, 1

# 뱀이 있는 곳은 2
coordinates[x][y] = 2

# 초기 방향은 동쪽
direction = 0

# 다음 회전 정보 Index
next_direction = 0

# 현재 시간
time = 0

# 뱀이 차지하고 있는 좌표 위치
body = [(x, y)]

while True:
    # 시간 추가
    time += 1

    # 다음 좌표
    next_x = x + dx[direction]
    next_y = y + dy[direction]

    # 맵 내부에 있음
    # 뱀의 몸통 좌표가 아님
    if 1 <= next_x <= n and 1 <= next_y <= n and coordinates[next_x][next_y] != 2:
        
        # 사과 있음(기존 꼬리 그대로 두고 추가)
        if coordinates[next_x][next_y] == 1:
            # 뱀이 차지하고 있는 좌표로 지정
            coordinates[next_x][next_y] = 2
            body.append((next_x, next_y))
        else:
            # 사과 없음(그냥 이동만)
            coordinates[next_x][next_y] = 2
            body.append((next_x, next_y))

            prev_x, prev_y = body.pop(0)
            coordinates[prev_x][prev_y] = 0
        
        x = next_x
        y = next_y

        # 방향 전환 필요
        if next_direction < len(directions) and directions[next_direction][0] == time:
            if directions[next_direction][1] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4

            next_direction += 1
        
    else:
        break

print(time)

