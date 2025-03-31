def binary_search(array: list, target: int, start: int, end: int):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return target
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(binary_search(array, 4, 0, len(array) - 1))


import bisect

index = bisect.bisect_left(array, 4)
print(array[index])