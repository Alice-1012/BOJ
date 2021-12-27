import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
deci_cnt = 0

for i in nums:
    cnt = 0
    if (i==1):
        continue
    for j in range (2, i+1):
        if (i%j)==0:
            cnt+=1
    if cnt ==1:
        deci_cnt+=1
print(deci_cnt)
            
