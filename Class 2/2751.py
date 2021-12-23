import sys
input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    a = int(input())
    result.append(a)
result.sort(reverse = False)

for i in range(n):
    print(result[i])
