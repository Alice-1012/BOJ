#1
n = int(input())
car = list(map(int,input().split()))
print(car.count(n))

#2
n = int(input())
car = list(map(int, input().split()))
cnt = 0
for i in car:
  if n == i:
    cnt+=1
print(cnt)
