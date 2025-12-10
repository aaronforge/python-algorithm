data = input().split('-')
result = sum(map(int, data[0].split('+')))

for d in data[1:]:
    result -= sum(map(int, d.split('+')))

print(result)












































# data = input().split('-')

# result = sum(map(int, data[0].split('+')))

# for d in data[1:]:
#     result -= sum(map(int, d.split('+')))

# print(result)