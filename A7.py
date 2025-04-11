n = input()

# 중간 index
mid_index = int(len(n) / 2)

# 왼쪽
left = list(map(int, n[:mid_index]))
# 오른쪽
right = list(map(int, n[mid_index:]))

# 일치함
is_possible = sum(left) == sum(right)

if is_possible:
    print("LUCKY")
else:
    print("READY")
