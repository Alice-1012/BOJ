import sys

n = int(input())
for i in range (n):
    p_str = sys.stdin.readline().strip()
    p_list = list(p_str)
    cnt = 0
    for j in p_list:
        if j =='(':
            cnt+=1
        elif j ==')':
            cnt-=1
        if cnt < 0:
            
            break
    if cnt ==0:
        print('YES')
    else:
        print('NO')
    
