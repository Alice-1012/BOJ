m = int(input())
n = int(input())

nums = []
i = 1
while i**2<=n:
    if m<=i**2<=n:
        nums.append(i**2)
    i+=1
if not nums:
    print(-1)
else:
    print(sum(nums))
    print(nums[0])
