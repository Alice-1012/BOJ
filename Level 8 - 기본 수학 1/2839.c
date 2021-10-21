#include <stdio.h>

int main()
{
    int n,cnt=0;
    scanf("%d",&n);
    
    while(1){
    	if(n%5==0)//n이 5의 배수일 경우 cnt에 몫을 더하고 break
    	{
    		cnt+=n/5;
    		break;
    	}
    	n-=3;//n이 5의 배수가 아닐 경우 n-3
    	cnt++;//3kg의 설탕봉지 개수가 1개 추가됨
    	if(n<=0) break;//계속 반복하다가 n이 0이하면 break;
        //n=0일 땐 3과 5의 조합으로 나누어 떨어짐, n<0일 땐 나누어 떨어지지 않음
    }
    if(n<0) printf("-1");
    else printf("%d",cnt);
    
}
