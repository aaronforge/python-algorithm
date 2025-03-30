array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array: list, start: int, end: int):
    # 원소가 1개 이하인 경우
    if start >= end:
        return

    # Index
    pivot = start
    left = pivot + 1
    right = end

    # 왼쪽 포인터가 오른쪽 포인터 보다 작거나 같아야 함
    while left <= right:
        
        # 왼쪽 포인터의 수가 피벗 값 보다 작은 경우 포인터 이동
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 오른쪽 포인터의 수가 피벗 값 보다 큰 경우 포인터 이동
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 포인터가 교차된 경우
        if left > right:
            # 작은 수와 피벗 위치를 교체
            array[pivot], array[right] = array[right], array[pivot]
        else:
            # 작은 수와 큰 수의 위치를 교체
            array[left], array[right] = array[right], array[left]
    
    # 피벗 분할 후 왼쪽 부분 정렬
    quick_sort(array, start, right - 1)

    # 피벗 분할 후 오른쪽 부분 정렬
    quick_sort(array, right + 1, end)
    

quick_sort(array, 0, len(array) - 1)
print(array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array: list):
    if len(array) < 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)

print(quick_sort2(array))