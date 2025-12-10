from collections import deque


n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]


dx = [-1, 1, 0, 0,]
dy = [0, 0, -1, 1,]


def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))
    

bfs(0, 0)
print(maze[n-1][m-1])


























































# from collections import deque


# n, m = map(int, input().split())
# maze = [list(map(int, list(input()))) for _ in range(n)]

# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     q = deque([(x, y)])

#     while q:
#         x, y = q.popleft()

#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
            
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
            
#             if maze[nx][ny] == 1:
#                 maze[nx][ny] = maze[x][y]+1
#                 q.append((nx, ny))


# bfs(0, 0)
# print(maze[n-1][m-1])
