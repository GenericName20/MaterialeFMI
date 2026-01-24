#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,n,mask,xset,xreset,xtoggle;
    scanf("%d%d",&x,&n);
    mask=1<<n;
    xset = x|mask;
    printf("%d\n",xset);
    xreset = ~((~x)|mask);
    printf("%d\n",xreset);
    xtoggle = x^mask;
    printf("%d",xtoggle);
    return 0;
}
