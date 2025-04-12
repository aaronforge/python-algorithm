from itertools import combinations

n, m = map(int, input().split())

# 치킨집과 집 좌표 정보
chickens = []
houses = []

for r in range(n):
    # 지도 입력
    data = list(map(int, input().split()))

    # 집, 치킨집 좌표 정보 추가
    for c in range(n):
        if data[c] == 1:
            houses.append((r, c))
        if data[c] == 2:
            chickens.append((r, c))

# 치킨집 M 개씩 묶은 경우의 수
comp = list(combinations(chickens, m))

result = 1e9

for combination in comp:
    combination_result = 0

    # 집에서 가장 가까운 치킨집 좌표 확인
    for hx, hy in houses:
        tmp = 1e9

        for cx, cy in combination:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        
        combination_result += tmp
    
    result = min(result, combination_result)
            

    

print(result)
