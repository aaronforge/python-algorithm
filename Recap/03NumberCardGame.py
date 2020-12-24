m, n = map(int, input().split())

answer = 0

for i in range(m):
    cards = list(map(int, input().split()))
    answer = max(answer, min(cards))

print(answer)
