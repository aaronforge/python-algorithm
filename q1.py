n = int(input())
people = list(map(int, input().split()))
people.sort()

group_count = 0
member_count = 0

for scary in people:
    member_count += 1

    if member_count >= scary:
        group_count += 1
        member_count = 0

print(group_count)
