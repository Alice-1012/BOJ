import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range (n):
    a,b = map(int, input().split())
    result.append([a,b])
    
result.sort(key = lambda x : (x[1],x[0]))

for i in result:
            print(i[0], i[1])
