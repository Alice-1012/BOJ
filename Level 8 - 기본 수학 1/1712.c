#include <stdio.h>

int main(){
    int a,b,c;
    int n;
    scanf("%d %d %d",&a,&b,&c);
    
    if(b>=c)
    {
        printf("-1");
    }
    else
    {
        n=a/(c-b)+1;
        printf("%d",n);
    }
    
}
