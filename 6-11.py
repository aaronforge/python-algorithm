import sys
input = sys.stdin.readline

n = int(input().strip())
data = []

for _ in range(n):
    # 성적 입력
    name, score = input().strip().split()
    data.append((name, int(score)))

# 성적 순 오름차순 정렬
data = sorted(data, key=lambda student: student[1])
    
print(' '.join([data_set[0] for data_set in data]))