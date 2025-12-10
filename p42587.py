from collections import deque


def solution(priorities, location):
    q = deque([])
    
    for idx, p in enumerate(priorities):
        q.append((idx, p))
    
    answer = 0
    
    while q:
        idx, p = q.popleft()
        
        if q and max(q, key=lambda x: x[1]) > p:
            q.append((idx, p))
        else:
            answer += 1
            if idx == location:
                break
    
    return answer
    

print(solution([2, 1, 3, 2], 2))