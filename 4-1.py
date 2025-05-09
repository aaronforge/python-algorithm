x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
command_types = ['L', 'R', 'U', 'D']

n = int(input())
commands = input().split()

for command in commands:
    command_index = command_types.index(command)

    next_x = x + dx[command_index]
    next_y = y + dy[command_index]

    # 영역 벗어남
    if next_x < 1 or next_y < 1 \
        or next_x > n or next_y > n:
        continue

    x = next_x
    y = next_y

print(x, y)
