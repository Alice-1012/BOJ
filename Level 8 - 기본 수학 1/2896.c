#include <stdio.h>

int main(){
    
    int a,b,v,d;
    scanf("%d %d %d",&a,&b,&v);
    if((v-b)%(a-b)==0)
    {
        d=(v-b)/(a-b);
    }
    else
    {
        d=(v-b)/(a-b)+1;
    }
    printf("%d",d);
}
