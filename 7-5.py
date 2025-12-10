import sys


input = lambda: sys.stdin.readline().rstrip()

n = int(input())
parts = list(map(int, input().split()))
parts.sort()

m = int(input())
needs = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for need in needs:
    idx = binary_search(parts, need, 0, n)

    if idx is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
