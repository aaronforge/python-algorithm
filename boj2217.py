# 10, 15 => 10과 15 중 작은 10을 기준으로 * n 개 하여 들면 최대 20kg 까지 가능
# 10, 15, 20 => 10 * n 하면 30, 15*2(15kg, 20kg 로프로만)하면 30
# 5, 15, 20, 40 => 5*n=20, 15*3=45, 20*2=40, 40*1=40
# 정렬하고 index loop 돌리면서 해당 index 포함 이후의 길이와 index의 원소 곱해서 max 값 갱신

n = int(input())
ropes = sorted(int(input()) for _ in range(n))

result = 0
for i in range(n):
    result = max(result, ropes[i] * (n - i))

print(result)
