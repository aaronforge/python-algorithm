from collections import deque


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(start):
    visited = [False] * (n+1)
    result = []
    
    def _dfs(x):
        visited[x] = True
        result.append(x)
        
        for v in graph[x]:
            if not visited[v]:
                _dfs(v)
    
    _dfs(start)

    return result


def bfs(start):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    result = []

    while q:
        x = q.popleft()
        result.append(x)
        
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return result


print(*dfs(v))
print(*bfs(v))

































# from collections import deque


# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for g in graph[1:n+1]:
#     g.sort()


# def dfs(start):
#     visited = [False] * (n+1)
#     result = []

#     def _dfs(x):
#         visited[x] = True
#         result.append(x)

#         for v in graph[x]:
#             if not visited[v]:
#                 _dfs(v)

#     _dfs(start)
    
#     return result



# def bfs(start):
#     visited = [False] * (n+1)
#     q = deque([start])
#     visited[start] = True
#     result = []

#     while q:
#         x = q.popleft()
#         result.append(x)

#         for v in graph[x]:
#             if not visited[v]:
#                 visited[v] = True
#                 q.append(v)
    
#     return result



# print(*dfs(v))
# print(*bfs(v))
