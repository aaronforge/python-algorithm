n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)

print(' '.join(map(str, data)))
