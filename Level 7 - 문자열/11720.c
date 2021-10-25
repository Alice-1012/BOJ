#include <stdio.h>

int main(){
	int n,sum=0;
	scanf("%d",&n);
	char a[n];
	scanf("%s", a);//문자열은 &를 쓰지 않아도 된다.
    for(int i = 0; i < n; i++){
        sum += a[i] - '0';
    }
    printf("%d",sum);

}
