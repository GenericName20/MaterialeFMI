#include <stdio.h>
#include <stdlib.h>
// n*8, n/4 si n*10
int main()
{
    int n;
    scanf("%d",&n);
    printf("%d\n",n<<3);
    printf("%d\n",n>>2);
    printf("%d",5*n<<1);
    return 0;
}
