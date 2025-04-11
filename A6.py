import heapq


def solution(food_times: list[int], k: int):
    if sum(food_times) <= k:
        return -1

    q = []

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    seconds = 0
    prev = 0
    food_count = len(food_times)

    while seconds + ((q[0][0] - prev) * food_count) < k:
        now = heapq.heappop(q)[0]

        seconds += (now - prev) * food_count
        food_count -= 1
        prev = now
    
    # Index 순 정렬
    result = sorted(q, key=lambda x: x[1])

    # 남은시간
    remaining = k - seconds
    next_index = remaining % food_count

    return result[next_index][1]



print(solution([3, 1, 2], 5))
print(solution([8, 6, 4], 15))
