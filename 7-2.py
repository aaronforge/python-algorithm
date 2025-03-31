def binary_search(array: list, target: int, left: int=0, right: int=None):
    if right is None:
        right = len(array) - 1
    
    if left > right:
        return None
    
    mid = (left + right) // 2

    if array[mid] > target:
        return binary_search(array, target, left, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, right)
    else:
        return mid


print(binary_search([0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 4))