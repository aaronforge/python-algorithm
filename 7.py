import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

def dfs(x: int, y: int):
    # 탐색 불가
    if x >= n or x < 0 or y >= m or y < 0:
        return False

    # 미탐색 영역
    if graph[x][y] == 0:
        graph[x][y] = 1

        # 값이 0인 미탐색 상하좌우 좌표를 돌면서
        # 0이 아닌 값이 나올 때 까지 합칠 수 있는 영역 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    
    return False

result = 0

for x in range(n):
    for y in range(m):
        # 한 번 들어가서 확장 가능한 영역을 모두 탐색하므로
        # x, y 좌표에 대해 한번씩만 돌고 오면 됨
        if dfs(x, y) == True:
            result += 1

print(result)