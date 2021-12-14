#1 중첩 for문 사용(time over)
n, m = map(int,input().split())

for i in range(n,m+1):
  for j in range(2,i):
    if i%j ==0:
      break
    else:
      if j==i-1:
        print(i)
      else:
        continue

#2 제곱근 걸러내기
def isPrime(num):
    if num ==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i ==0:
                return False
        return True
n, m = map(int,input().split())

for i in range(n,m+1):
    if isPrime(i):
        print(i)
        
        
