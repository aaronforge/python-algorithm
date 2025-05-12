start = input()

x = ord(start[0].lower()) - ord('a') + 1
y = int(start[1])

directions = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

result = 0

for direction in directions:
    nx = x + direction[0]
    ny = y + direction[1]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
            result += 1

print(result)
