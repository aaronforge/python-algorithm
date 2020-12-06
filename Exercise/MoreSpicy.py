def solution(scoville, K):
    import heapq
    data = []

    for s in scoville:
        heapq.heappush(data, s)
        print(s)
        print(data)

    answer = 0

    while len(data) > 0:
        if data[0] >= K:
            return answer
        a = heapq.heappop(data)
        if data:
            b = heapq.heappop(data)
            heapq.heappush(data, a + (b * 2))
        answer += 1
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
