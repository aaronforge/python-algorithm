n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0

for s, e in times:
    if s >= end:
        end = e
        count += 1

print(count)





















































# n = int(input())
# schedules = [list(map(int, input().split())) for _ in range(n)]
# schedules.sort(key=lambda x: (x[1], x[0]))

# count = 0
# end = 0

# for s, e in schedules:
#     if s >= end:
#         end = e
#         count += 1

# print(count)
