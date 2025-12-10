from functools import cmp_to_key

from collections import deque


def solution(priorities, location):
    # (0, 2), (1, 1), (2, 3), (3, 2)
    # A(2) B(1) C(3) D(2)
    # => B C D A => C D A B => C 실행 => D A B => D 실행 => A 실행 => B 실행
    # => location 2에 있던 작업 우선순위 = 3 가장 먼저 실행 됨 => 1 리턴
    
    # (0, 1) (1, 1) (2, 9) (3, 1) (4, 1) (5, 1)
    # (0, 1) => (1, 1) (2, 9) (3, 1) (4, 1) (5, 1) (0, 1)
    # (1, 1) => (2, 9) (3, 1) (4, 1) (5, 1) (0, 1) (1, 1)
    # 실행 1 (2, 9) => (3, 1) (4, 1) (5, 1) (0, 1) (1, 1)
    # 실행 2~ (3, 1) (4, 1) (5, 1) (0, 1) (1, 1)
    
    q = deque([])
    
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    cnt = 1
    
    while q:
        i, p = q.popleft()
        
        max_p = max(q, key=lambda x: x[1])[1]
        if max_p > p:
            q.append((i, p))
        else:
            if i == location: break
            cnt += 1
        
        
    
    return cnt

print(solution([2, 1, 3, 2], 2))