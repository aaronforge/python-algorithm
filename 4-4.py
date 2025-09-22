n, m = map(int, input().split())
x, y, d = map(int, input().split())

visits = [[0] * m for _ in range(n)]

fields = []
for _ in range(n):
    row = list(map(int, input().split()))
    fields.append(row)

# 0 북 / 1 동 / 2 남 / 3 서
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

def turn_left():
    global d
    d -= 1

    if d == -1:
        d = 3

turn_count = 0
visit_count = 1
visits[x][y] = 1

while True:
    turn_left()

    next_x = x + dx[d]
    next_y = y + dy[d]

    if visits[next_x][next_y] == 0 \
        and fields[next_x][next_y] == 0 \
        and next_x > 0 and next_y > 0 \
        and next_x <= n and next_y <= m:
            x, y = next_x, next_y
            visit_count += 1
            continue

    turn_count += 1

    if turn_count == 4:
        next_x = x - dx[d]
        next_y = y - dy[d]

        # 뒤로 한 칸(북 <-> 남, 동 <-> 서) 가능
        if fields[next_x][next_y] == 0:
             x, y = next_x, next_y
        else:
             break
        
        turn_count = 0

print(visit_count)
         
