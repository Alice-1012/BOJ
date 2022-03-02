N = int(input())
nums = []
for i in map(int,str(N)):
  nums.append(i)
nums.sort(reverse=True)
for i in range(0,len(nums)):
  print(nums[i],end='')
