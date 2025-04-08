import sys


input = lambda: sys.stdin.readline().rstrip()


s = input()

group0 = 0
group1 = 0

if s[0] == '0':
    group0 += 1
else:
    group1 += 1

current_char = s[0]

for char in s:
    if char != current_char:
        if char == '0':
            group0 += 1
        else:
            group1 += 1

        current_char = char

print(min(group0, group1))