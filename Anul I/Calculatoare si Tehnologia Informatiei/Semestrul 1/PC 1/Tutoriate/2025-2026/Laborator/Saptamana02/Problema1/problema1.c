#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int v[18];
    scanf("%d",&n);
    int i=0;
    while(n>0){
        v[i]=n%2;
        i++;
        n/=2;
    }
    for(int j=i-1;j>=0;j--){
        printf("%d",v[j]);
    }
    return 0;
}
