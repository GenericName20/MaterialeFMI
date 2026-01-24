#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sumcif(int n)
{
    int sum=0;
    while(n!=0)
    {
        sum+=n%10;
        n/=10;
    }
    return sum;
}

int main()
{
    int x=1,lastx,per=0;
    while(x!=0)
    {
        scanf("%d", &x);
        if(lastx%sumcif(lastx)==x && x!=0)
        {
            per++;
            printf("perechea %d %4d %4d \n",per,lastx,x);
        }
        lastx=x;
    }
    return 0;
}
