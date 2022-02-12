import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

t = int(input())

# 지렁이 이동
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(graph, y, x):
    queue = deque()
    queue.append([y, x])
    graph[y][x] = 0

    while queue:
        now_y, now_x = queue.popleft()
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1:
                    queue.append([ny, nx])
                    graph[ny][nx] = 0


# 테스트케이스
for _ in range(t):
    # 가로길이 m, 세로길이 n, 배추개수 k
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    # 배추입력
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 지렁이 수
    count = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                count += 1
                dfs(graph, y, x)

    print(count)
