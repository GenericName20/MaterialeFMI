#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,rez=0;
    printf("Dati valoare la n:");
    scanf("%d",&n);
    while(n%2==0){
        n=n>>1;
        rez++;
    }
    if(n==1)
        printf("Numarul n este de forma n=2^%d",rez);
    else
        printf("Numarul n NU este de forma n=2^k");
    return 0;
}
