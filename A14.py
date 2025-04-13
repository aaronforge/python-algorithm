from itertools import permutations


def solution(n: int, weak: list[int], dist: list[int]):
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1

    # 투입 시점 = 취약 지점
    for start in range(length):
        # 각 친구 나열 순서에 따른 모든 경우의 수 확인
        for friends in permutations(dist, len(dist)):
            count = 1

            # 가능한 마지막 위치
            position = weak[start] + friends[count - 1]

            for i in range(start, start + length):
                # 가능 범위 벗어남
                if position < weak[i]:
                    count += 1
                    
                    if count > len(dist):
                        # 친구 투입 불가
                        break
                    
                    position = weak[i] + friends[count - 1]
            
            answer = min(answer, count)

    return answer if answer <= len(dist) else - 1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) # should be 2
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7])) # should be 1