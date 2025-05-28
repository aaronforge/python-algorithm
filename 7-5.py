n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
req = list(map(int, input().split()))
req.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for r in req:
    if binary_search(data, r, 0, n - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
