#1 Counter 사용
from collections import Counter

N = int(input())
card1 = list(map(int, input().split()))
cnt = Counter(card1)

M = int(input())
card2 = list(map(int, input().split()))

for i in card2:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0, end=' ')


#2 dict 직접 만들기
import sys

N = int(input())
card1 = list(map(int, sys.stdin.readline().split()))

cnt = dict()

for i in card1:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

M = int(input())
card2 = list(map(int, sys.stdin.readline().split()))

for i in card2:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0, end=' ')


    
