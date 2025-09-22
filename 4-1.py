size = int(input())
commands = input().split()
x, y = 1, 1

# L R U D 순
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

for command in commands:
    if command == 'L':
        direction_index = 0
    elif command == 'R':
        direction_index = 1
    elif command == 'U':
        direction_index = 2
    elif command == 'D':
        direction_index = 3
    else:
        continue

    next_x = x + dx[direction_index]
    next_y = y + dy[direction_index]

    if next_x < 1 or next_y < 1:
        continue
    if next_x > size or next_y > size:
        continue
    
    x = next_x
    y = next_y


print(x, y)