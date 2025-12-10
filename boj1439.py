data = input()

zero = 0
one = 0

current = data[0]

if current == '0':
    zero += 1
else:
    one += 1

for d in data[1:]:
    if d != current:
        current = d
        if d == '0':
            zero += 1
        else:
            one += 1

print(min(zero, one))








































# s = input()

# zero = 0
# one = 0

# current = s[0]
# if current == '0':
#     zero += 1
# else:
#     one += 1

# for c in s[1:]:
#     if current != c:
#         current = c
        
#         if current == '0':
#             zero += 1
#         else:
#             one += 1

# print(min(zero, one))
