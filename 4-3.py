start = input()

coordinates = [
    (-2, -1),
    (-2, +1),
    (+2, +1),
    (+2, -1),
    (-1, +2),
    (+1, +2),
    (-1, -2),
    (+1, -2)
]

x = ord(start[0]) - ord('a') + 1
y = int(start[1])

count = 0

for target in coordinates:
    dx, dy = target
    next_x = x + dx
    next_y = y + dy

    if next_x < 1 or next_y < 1:
        continue
    if next_x > 8 or next_y > 8:
        continue

    count += 1

print(count)
