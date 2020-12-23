def solution():
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = 0

    numbers.sort()
    big = numbers[n - 1]
    small = numbers[n - 2]

    big_count = (m // (k + 1) * k) + (m % (k + 1))

    answer += big_count * big
    answer += (m - big_count) * small

    return answer


print(solution())

# 5 8 3
# 2 4 5 4 6
# 6 6 6 5 / 6 6 6 5
# ==> 46

# 7 7 2
# 1 2 3 4 5 6 7
# 7 7 6 / 7 7 6 / 7
# ==> 47
