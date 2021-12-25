#1 직관적 코드 ( 시간초과 )
import sys
input = sys.stdin.readline()

n = int(input)
a = list(map(int,input.split()))
a.sort()
m = int(input)
x = list(map(int, input.split()))

for i in range (n):
  if m_arr[i] in n_arr:
    print(1)
  else:
    print(0)
   
  
#2 이진탐색
import sys

def BinarySearch(a,x):
    start = 0
    end = len(a)-1
    while start<=end:
        mid = (start+end)//2
        if x==a[mid]:
            return 1
        elif x>a[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0

n = int(input())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

m = int(input())
x = list(map(int, sys.stdin.readline().split()))

for i in range (m):
    print(BinarySearch(a,x[i]))
