#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    if((n|1)>n)
        printf("PAR");
    else
        printf("IMPAR");
    return 0;
}
