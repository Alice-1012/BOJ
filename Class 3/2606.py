n = int(input()) #노드의 개수
m = int(input()) #간선의 개수

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)
