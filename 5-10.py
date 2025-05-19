n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    # 벗어남
    if x < 0 or y < 0 \
        or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1

        # 연결된 상하좌우 방문 처리
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True


    return False


result = 0
for i in range(n):
    for j in range(m):
        # 묶음 방문처리
        if dfs(i, j) == True:
            result += 1

print(result)