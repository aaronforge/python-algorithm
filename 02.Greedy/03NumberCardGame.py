def solution():
    n, m = map(int, input().split())
    answer = 0

    for i in range(n):
        row = list(map(int, input().split()))
        answer = max(answer, min(row))

    return answer


print(solution())
