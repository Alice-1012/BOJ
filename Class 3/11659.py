import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
num = list(map(int, input().split()))
nums = [0]
 
temp = 0    
for i in num:
    temp += i
    nums.append(temp)
 
for i in range(m):
    a, b = map(int, input().split())
    print(nums[b] - nums[a-1])
