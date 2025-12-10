n = int(input())
amounts = list(map(int, input().split()))

d = [0] * n

# 0 부터 시작해서 최대 값으로 갱신
d[0] = amounts[0]
d[1] = max(amounts[0], amounts[1])

for i in range(2, n):
    # 이전 창고 양 vs 현재 창고와 전전 창고의 양을 합친 것 중 큰 값으로 최댓값 갱신
    d[i] = max(d[i-1], amounts[i] + d[i-2])

print(d[n-1])
