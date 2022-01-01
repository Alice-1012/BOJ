#1 시간초과 
n = int(input())
result = []
for i in range(n):
    a = int(input())
    result.append(a)
result.sort()

for i in range(n):
    print(result[i])
    
#2 
import sys

N = int(input())
nums = [0]*10001

for _ in range(N):
    nums[int(sys.stdin.readline())] +=1
    
for i in range(10001):
    if nums[i]!=0:
        for j in range(nums[i]):
            print(i)
