import sys


input = lambda: sys.stdin.readline().rstrip()


# 동전 수
n = int(input())

# 갖고 있는 동전
coins = list(map(int, input().split()))

coins.sort()

target = 1

for coin in coins:
    print(target, coin)
    
    if target < coin:
        break


    target += coin


print(target)
