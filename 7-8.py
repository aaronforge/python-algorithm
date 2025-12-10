import sys


input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    mid = (start + end) // 2
    
    total = 0

    # 자른 뒤 남게 되는 떡 길이 더하기
    for x in array:
        if x > mid:
            total += x - mid
    
    # 길이가 부족한 경우 더 잘라야 함(왼쪽으로 mid 이동 필요)
    if total < m:
        end = mid - 1
    # 길이가 부족한 경우 최대 수치를 구해야 함(오른쪽으로 mid 이동 필요)
    else:
        result = mid
        start = mid + 1

print(result)
        
