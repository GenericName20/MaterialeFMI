#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n,nrr=0,i=0,j=0;
    scanf("%d",&n);
    for(i=0;i<=n;i++)
    {
        for(j=i+1;j<=n-i;j++)
        {
            int a=i,b=j,c=n-i-j;
            if(a+b>c && c+b>a && c+a>b && a!=b && b!=c && c!=a)
            {
                nrr++;
                printf("Perechea %d : (%d,%d,%d)\n",nrr,a,b,c);
            }
        }
    }
    return 0;
}