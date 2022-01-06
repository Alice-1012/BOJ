import sys

n, m = map(int, sys.stdin.readline().split())
wood = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(wood)

result = 0

while (start<=end):
    sum = 0
    mid = (start+end)//2
    for x in wood:
        if x>mid:
            sum +=x-mid
    if sum<m:
        end = mid-1
    else:
        result = mid
        start = mid+1
        
print(result)
