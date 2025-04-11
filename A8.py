s = sorted(input())

# 문자열만 배열로 추출
chars = list(filter(lambda x: x.isalpha(), s))
# 숫자만 추출
nums = list(map(int, filter(lambda x: x.isdigit(), s)))

# 합치기
result = ''.join(chars) + str(sum(nums))

print(result)
