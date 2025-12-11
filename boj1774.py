n = int(input())

positives = []
negatives = []

result = 0

for _ in range(n):
    num = int(input())

    if num > 1:
        # 1보다 큰 값
        positives.append(num)
    elif num <= 0:
        # 0과 음수(음수 한개, 0 한개 남으면 곱해서 0으로 만들어버리기 위함)
        negatives.append(num)
    else:
        # 1은 더해버리기
        result += 1

positives.sort(reverse=True)
negatives.sort()

# 양수
for i in range(0, len(positives), 2):
    if i < len(positives)-1:
        result += positives[i] * positives[i+1]
    else:
        result += positives[i]

# 음수
for i in range(0, len(negatives), 2):
    if i < len(negatives)-1:
        result += negatives[i] * negatives[i+1]
    else:
        result += negatives[i]

print(result)
