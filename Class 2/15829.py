L = int(input())
M = 1234567891
r = 31
sum = 0
nums = input()

for i in range(len(nums)):
  num = ord(nums[i])-96
  sum+=num*(r**i)

print(sum%M)
