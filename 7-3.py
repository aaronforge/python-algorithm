def while_binary_search(array: list, target: int, left: int = 0, right: int = None):
    # 우측점 없음 > 배열 마지막 인덱스 지정
    if right is None:
        right = len(array) - 1

    # 좌측점이 우측점 보다 같거나 작은 동안
    while left <= right:
        mid = (left + right) // 2

        # 중간점 = 대상
        if array[mid] == target:
            return mid
        # 중간점이 대상 보다 큼 > 좌측 배열 탐색
        elif array[mid] > target:
            right = mid - 1
        # 이외의 경우 > 우측 배열 탐색
        else:
            left = mid + 1
        
    return None

print(while_binary_search([1, 3, 5, 7, 9, 11, 13], 5))