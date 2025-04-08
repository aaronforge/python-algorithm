import sys


input = lambda: sys.stdin.readline().rstrip()


# def get_next_food(food_times: list[int], x: int):
#     if sum(food_times) == 0:
#         return -1
    
#     index = x // len(food_times)

#     if food_times[index] == 0:
#         food_times[index] = get_next_food(food_times, x + 1)
    
#     return food_times[index]


# def get_result(food_times: list[int], k: int):
#     result = 0

#     for i in range(k):
#         index = i % len(food_times)
#         print(food_times, index, i)

#         # 먹을 수 있는 상태
#         if food_times[index] > 0:
#             food_times[index] -= 1
#         else:
#         # 먹을 수 없는 상태
#         # TODO: 다음으로 먹을 수 있는 음식을 찾아야 함
#         # TODO: 먹을 수 없는 상태면 탈출해야 함
#             next_food = get_next_food(food_times, index)
#             print(food_times, next_food, '?')
#             if next_food >= 0:
#                 food_times[next_food] -= 1
#                 print(food_times, next_food, '!')

#     return result


# print(get_result([3, 1, 2], 5))

import heapq


food = [3, 1, 2]
k = 5

def solution(food: list[int], k: int):
    if sum(food) <= k:
        return -1
    
    queue = []

    for i, time in enumerate(food):
        heapq.heappush(queue, (time, i + 1))
    
    # 총 걸린 시간
    total_time = 0

    # 이전 단계 까지 시간
    prev_time = 0

    # 음식 수
    food_count = len(food)

    while queue:
        t, _ = queue[0]
        cost = (t - prev_time) * food_count

        if total_time + cost > k:
            # 오류 정상화됨
            break

        total_time += cost
        prev_time = t

        heapq.heappop(queue)
        food_count -= 1
    
    result = sorted(queue, key=lambda x: x[1])
    return result[(k - total_time) % food_count][1]


print(solution(food, k))
     