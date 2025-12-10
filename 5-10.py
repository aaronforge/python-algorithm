n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        # 연결된 상하좌우 탐색
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1


print(result)
