n = int(input())

data = [input().split() for _ in range(n)]

data.sort(key=lambda data_set: int(data_set[1]))

print(' '.join([x[0] for x in data]))
