import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = list(map(int, input().split()))

left = 0
# 떡의 최대 길이
right = max(array)

result = 0

# 0 부터 떡의 최대 길이만큼 모든 떡을 자르면서
# 잘린 부분의 합이 m이 나올 때 까지 이진탐색
while left <= right:
    # 중간점
    mid = (left + right) // 2

    total = 0

    # 떡 길이 비교
    for length in array:
        # 떡이 더 길기 때문에 자를 수 있음
        if length > mid:
            total += length - mid
    
    # 합이 요청한 길이 보다 짧음 -> 왼쪽으로 이동
    if total < m:
        right = mid - 1
    # 이외의 경우 -> 우측으로 이동
    else:
        left = mid + 1

        # 절단기 높이 최대값 갱신
        result = mid

print(result)
