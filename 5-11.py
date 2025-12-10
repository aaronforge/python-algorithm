from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우 좌표
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 범위 벗어남
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            # 괴물 있음(벽 취급)
            if graph[nx][ny] == 0:
                continue

            # 첫방문 시 방문 거리 계산(직전 좌표 값 + 1 = 이동하기 위해 거친 노드의 갯수)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    
    return graph[n-1][m-1]


print(bfs(0, 0))
