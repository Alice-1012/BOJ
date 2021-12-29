#1 더 간결하게 짤 수는 없던거니 과거의 나...?
n = int(input())

for i in range(n):
    H,W,N = map(int,input().split())
    floor = 0
    ho = 0
    if N % H ==0:
        H-=1
        ho = (N//H)-1
        print(101+ho+(H*100))
    else:
        floor = (N%H)-1
        ho = N//H
        print(101+ho+(floor*100))
        
#2 좀 복잡한 듯 보여서 찾아본 간결한 코드!
n = int(input())

for i in range(n):
    H,W,N = map(int,input().split())
    num = N//H + 1
    floor = N % H
    if N % H ==0:
        num = N//H
        floor = H
    print(f'{floor*100+num}')
    
==> 초기에 작성한 코드도 결국 알고리즘순서는 맞아서 나름 뿌듯! 
