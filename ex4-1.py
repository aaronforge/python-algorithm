import sys
input = sys.stdin.readline

# 좌표 정보 Set
controls = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

n = int(input())
input_keys = list(input().split())

position = [1, 1]

# 입력 키 Loop
for key in input_keys:
    key = key.upper()

    # 입력 Key Index
    control_idx = controls.index(key)

    # 이동이 필요한 좌표 수치
    x = dx[control_idx]
    y = dy[control_idx]

    # 다음 예정 좌표
    next_x = position[0] + x
    next_y = position[1] + y

    if next_x < 1 or next_y < 1 or next_x > n or next_y > n:
        # 영역 침범(무시)
        continue

    # 정상인 경우 진행(좌표 현경)
    position[0] = next_x
    position[1] = next_y
    
print(position[0], position[1])