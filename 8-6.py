import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
storage = list(map(int, input().split()))

a = [0] * 100

a[0] = storage[0]
a[1] = max(storage[0], storage[1])

for i in range(2, n):
    a[i] = max(storage[i - 1], storage[i - 2] + storage[i])

print(a[n - 1])