#include <iostream>

using namespace std;

int main()
{
    int x,n,mask,xset,xdelete,xswap;
    scanf("%d%d",&x,&n);
    mask=1<<n;
    xset = x|mask;
    printf("%d\n",xset);
    xdelete = ~((~x)|mask);
    printf("%d\n",xdelete);
    xswap = x^mask;
    printf("%d",xswap);
    return 0;
}
