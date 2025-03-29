import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 맵 좌표별 지형
map_coordinates = [list(map(int, input().split())) for _ in range(n)]

# 방문한 맵 좌표
visited_coordinates = [[0] * m for _ in range(n)]

# 첫 좌표 방문 처리
visited_coordinates[x][y] = 1

# 북동남서(direction 0, 1, 2, 3)에 따른 좌표 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def left_turn():
    global direction
    # 왼쪽으로 돌면 -1이 되어야 함 
    direction -= 1

    # 음수인 경우는 마지막 방향인 서쪽을 가르키게 됨
    if direction < 0:
        direction = 3

# 방문한 좌표 수(첫 좌표가 있으므로 1로 시작)
visit_count = 1

# 회전 수(4번이면 모든 곳 방문해봤음)
turn_count = 0

# 테스트 시작
while True:
    # 회전
    left_turn()

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 가보지 않았고 육지인 곳
    if visited_coordinates[nx][ny] == 0 and map_coordinates[nx][ny] == 0:
        # 이동
        visited_coordinates[nx][ny] = 1
        x = nx
        y = ny

        # 회전 수 초기화
        turn_count = 0
        visit_count += 1
        continue

    # 방문했거나 육지가 아닌 곳(추가 회전 필요함)
    else:
        turn_count += 1
    
    # 이미 모든 곳을 방문했거나 갈 수 있는 곳이 없는 경우
    if turn_count >= 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로가기 가능
        if map_coordinates[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤로가기 불가능(종료)
        else:
            break

        turn_count = 0

print(visit_count)
