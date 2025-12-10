coordinates = list(input())

x = ord(coordinates[0]) - ord('a')
y = int(coordinates[1]) - 1

directions = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
]

result = 0

for d in directions:
    nx = x + d[0]
    ny = y + d[1]

    if 0 <= nx <= 7 and 0 <= ny <= 7:
        result += 1

print(result)
