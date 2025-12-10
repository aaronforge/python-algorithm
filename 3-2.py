n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

first = array[-1]
second = array[-2]

num_of_repeats = m // (k + 1)

first_sum = first * k * num_of_repeats
second_sum = second * num_of_repeats

# 1번
result = first_sum + second_sum

# 나머지 남는 경우는 second 어차피 없음
remaining = m % (k + 1)
result += (remaining * first)

print(result)


# [Case 1]
# 5 8 3
# 2 4 5 4 6
# 6 6 6 5 | 6 6 6 5     => 46

# [Case 2]
# 5 9 3
# 2 4 5 4 6
# 6 6 6 5 | 6 6 6 5 | 6 => 52

# [Case 3]
# 5 7 3
# 2 4 5 4 6
# 6 6 6 5 | 6 6 6       => 41
