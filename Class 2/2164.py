#1 deque를 사용했지만 최선은 아니었던 것
from collections import deque
n = int(input())
nums = list(range(1,n+1))

deq = deque(nums)
while len(deq) >1 :
    deq.popleft()
    deq.rotate(-1)

print(deq[0])

#2 수학적 사고를 기르자...!

input = int(input()) 
square = 2 

while True:
    if (input == 1 or input == 2):
        print(input) 
        break
    square *= 2 
    if (square >= input):
        print((input - (square // 2)) * 2)
        break



