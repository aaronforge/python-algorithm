s = list(map(int, input()))

result = s[0]

for n in s[1:]:
    if result <= 1 or n <= 1:
        result += n
    else:
        result *= n

print(result)