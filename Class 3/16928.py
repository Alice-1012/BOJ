from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        for i in range(1, 7):
            n = node+i
            if n > 100:
                continue
            t = graph[n]
            if check[t] == -1:
                q.append(t)
                check[t] = check[node]+1
                if t == 100:
                    return ;
                
N, M = map(int, input().split())
graph = [i for i in range(101)]
for _ in range(N):
    u, v = map(int, input().split())
    graph[u] = v
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v
check = [-1]*101
bfs(1)
print(check[100])
