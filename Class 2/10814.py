#1 5152ms ( input().split())
n = int(input())

member_list = []
for _ in range (n):
    age, name = map(str,input().split())
    age = int(age)
    member_list.append((age,name))

member_list.sort(key = lambda x:x[0])

for i in member_list:
    print(i[0],i[1])
    
#2 296ms (sys.stdin.readline())
import sys 
n=int(sys.stdin.readline())

member_list = []
for _ in range (n):
    age, name = map(str,sys.stdin.readline().split())
    age = int(age)
    member_list.append((age,name))

member_list.sort(key = lambda x:x[0])

for i in member_list:
    print(i[0],i[1])
