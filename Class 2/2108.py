import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
num_list = []

for _ in range (n):
    num_list.append(int(input()))

def mean(a):
    return round(sum(a)/n)

def median(a):
    a.sort()
    return a[n//2]

def freq(a):
    cnt = Counter(a).most_common()
    if len(a)>1:
        if cnt[0][1]==cnt[1][1]:
            fre = cnt[1][0]
        else:
            fre = cnt[0][0]
    else:
        fre = cnt[0][0]
    return fre
        
def scope(a):
    return (a[-1] -  a[0])
    
    
print(mean(num_list))
print(median(num_list))
print(freq(num_list))
print(scope(num_list))
