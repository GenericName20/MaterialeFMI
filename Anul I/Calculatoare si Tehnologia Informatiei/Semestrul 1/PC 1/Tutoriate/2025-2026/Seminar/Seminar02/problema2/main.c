#include <stdio.h>
#include <stdlib.h>

int main()
{
    short int x, mask,k;
    scanf("%d %d",&x,&k);
    mask=(~(1<<k))&x;
    printf("%d\n",mask);
    x=x>>k;
    x=x|(mask<<k);
    printf("%d\n",x);
}
