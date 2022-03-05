import collections
m, n = map(int, input().split())
deq = collections.deque([])
answer = []

for i in range(m):
    deq.append(i+1)

while len(deq) != 0:
    for _ in range(n):
        x = deq.popleft()
        deq.append(x)
    answer.append(deq.pop())
print('<' + ', '.join(map(str,answer)) + '>')
