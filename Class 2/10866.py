from collections import deque
import sys

N = int(sys.stdin.readline())
deq = deque()
for _ in range (N):
    word = sys.stdin.readline().split()
    cmd = word[0]
    
    if cmd == 'push_front':
        deq.appendleft(int(word[1]))
        
    elif cmd == 'push_back':
        deq.append(int(word[1]))
        
    elif cmd == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
            
    elif cmd == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
            
    elif cmd == 'size':
        print(len(deq))
        
    elif cmd == 'empty':
        if deq:
            print(0)
        else:
            print(1)
            
    elif cmd == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
            
    elif cmd == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
