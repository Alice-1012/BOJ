N = input()
result = N

for i in range(0,N):
  word = input()
  for j in range(0,len(word)-1):
    result -=1
    break
    
print(result)
