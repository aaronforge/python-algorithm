from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

a = [[0] * (n + 1)]
d = [[0] * (n + 1) for _ in range(n + 1)]

# 배열 생성
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# 합배열 생성
for i in range(1, n + 1):
    for j in range(1, n + 1):
        d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = d[x2][y2] - d[x1-1][y2] - d[x2][y1 - 1] + d[x1 - 1][y1 - 1]
    print(result)