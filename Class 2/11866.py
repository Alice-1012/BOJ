# append 대신 deque의 rotate 함수 사용
from collections import deque

n, k = map(int,input().split())
deq = deque([])
for i in range(1, n + 1):
    deq.append(i)
print('<', end='')

while len(deq) >0:
    deq.rotate(-k)
    if len(deq) == 1:
        print('{}>'.format(deq.pop()))
    else:
        print('{},'.format(deq.pop()), end=' ')
  
