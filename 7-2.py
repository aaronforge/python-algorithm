def recursive_binary_search_index(array: list, target: int, left: int = 0, right: int = None):
    # 우측 기준 없으면 마지막 인덱스 지정
    if right is None:
        right = len(array) - 1
    
    # 왼쪽 기준이 오른쪽 기준점 넘어감
    if left > right:
        return None
    
    # 중간 지점(소수점 버림)
    mid = (left + right) // 2

    # 중간점 요소가 찾으려는 대상 보다 작음 > 중간점 기준 우측 배열 추가 탐색
    if array[mid] < target:
        return recursive_binary_search_index(array, target, mid + 1, right)
    # 중간점 요소가 찾으려는 대상 보다 큼 > 중간점 기준 좌측 배열 추가 탐색
    elif array[mid] > target:
        return recursive_binary_search_index(array, target, left, mid - 1)
    # 중간점 요소 = 대상
    else:
        return mid

print(recursive_binary_search_index([1, 3, 5, 7, 9, 11, 13], 5))