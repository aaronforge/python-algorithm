import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]


def dfs(x, y):
    # 범위 벗어남
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 칸막이가 존재하지 않아야 함
    if graph[x][y] == 0:
        # 이미 탐색 완료한 칸
        graph[x][y] = 1

        # 현재 칸 기준으로 상하좌우 재귀를 돌면서 연결된 0인 칸 모두 탐색 완료 처리
        dfs(x -1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        # 구멍이 뚫려있던 칸
        return True

    return False


result = 0

for x in range(n):
    for y in range(m):
        # 구멍이 뚫린 영역이 존재하는 칸
        if dfs(x, y) == True:
            result += 1

print(result)