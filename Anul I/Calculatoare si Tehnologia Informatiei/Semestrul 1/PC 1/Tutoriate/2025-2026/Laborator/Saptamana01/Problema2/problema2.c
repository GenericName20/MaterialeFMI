#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,c,rez;
    scanf("%d%d%d",&a,&b,&c);
    rez = ((b>c ? b : c)>(a>b ? a : b))?(b>c ? b : c):(a>b ? a : b);
    printf("%d",rez);
    return 0;
}
