n = int(input())
directions = input().split()

x, y = 1, 1

# L R U D
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, 1]


def get_direction_idx(d):
    if d == 'L': return 0
    elif d == 'R': return 1
    elif d == 'U': return 2
    elif d == 'D': return 3
    raise ValueError()

for d in directions:
    idx = get_direction_idx(d)

    nx = x + dx[idx]
    ny = y + dy[idx]

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(y, x)
