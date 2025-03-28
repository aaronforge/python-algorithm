import sys
input = sys.stdin.readline

point = input()

# Input 좌표
x = int(point[1])
y = int(ord(point[0])) - int(ord('a')) + 1

# 체스 판 사이즈
size = 8

# 움직임 좌표(2가지 4방향 => 8가지)
movements = [[2, 1], [2, -1],
             [-2, 1], [-2, -1],
             [1, 2], [-1, 2],
             [1, -2], [-1, -2]]

count = 0

for movement in movements:
    # 이동 명령 좌표
    movement_x = movement[0]
    movement_y = movement[1]

    # 다음 예정 좌표
    next_x = x + movement_x
    next_y = y + movement_y

    # 범위 벗어남
    if next_x < 1 or next_y < 1 or next_x > size or next_y > size:
        continue
    
    # 이동 가능
    count += 1

print(count)

