import sys
n = int(sys.stdin.readline())
room = []
for _ in range(n):
    time = list(map(int,sys.stdin.readline().split()))
    room.append(time)
room.sort(key = lambda x:(x[1],x[0]))

end = 0
cnt = 0
for i,j in room:
    if i>=end:
        cnt += 1
        end = j
        
print(cnt)
