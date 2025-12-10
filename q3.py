data = input()

zero_group = 0
one_group = 0
prev = data[0]

if prev == '0':
    zero_group += 1
else:
    one_group += 1

# 0001100 => 11 한번 뒤집어서 => 1회
# 001100011100 => 11, 111 한번씩 뒤집어서 0 => 2회
for c in data[1:]:
    if c != prev:
        if c == '0':
            zero_group += 1
        else:
            one_group += 1
        prev = c

print(min(zero_group, one_group))

