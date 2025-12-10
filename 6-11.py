n = int(input())

data = [input().split() for _ in range(n)]
rows = [(row[0], int(row[1])) for row in data]

rows.sort(key=lambda student: student[1])

print(' '.join([row[0] for row in rows]))
