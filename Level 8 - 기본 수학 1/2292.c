#include <stdio.h>

int main(){
    int n,i,a=1;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        a+=(i-1)*6;
        if(n<=a) break;
    }
    printf("%d\n",i);
    return 0;
}
