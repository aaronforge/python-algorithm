import sys
input = lambda: sys.stdin.readline().rstrip()


def while_binary_search_index(array: list, target: int, left: int = 0, right: int = None):
    """
    bisect 라이브러리를 활용해도 되지만 따로 구현해보는 이진탐색
    """
    
    # 우측점 미제공 시 배열 마지막 Index
    if right is None:
        right = len(array) - 1

    # 좌측점이 우측점을 만날 때 까지 반복
    while left <= right:
        # 중간점 Index
        mid = (left + right) // 2

        # 중간점 요소 = target
        if array[mid] == target:
            return mid
        # 중간점 요소가 target 보다 큼 -> 좌측 배열 탐색
        elif array[mid] > target:
            right = mid - 1
        # 이외의 경우 -> 우측 배열 탐색
        else:
            left = mid + 1

    return None


# 가게 부품 수
n = int(input())
# 가게 보유 부품 번호
in_store = list(map(int, input().split()))

# 주문 부품 수
m = int(input())
# 주문 부품 번호
order = list(map(int, input().split()))

# 이진탐색을 위한 sort
in_store.sort()

for element in order:
    index = while_binary_search_index(in_store, element)
    
    if index != None:
        print('yes')
    else:
        print('no')
