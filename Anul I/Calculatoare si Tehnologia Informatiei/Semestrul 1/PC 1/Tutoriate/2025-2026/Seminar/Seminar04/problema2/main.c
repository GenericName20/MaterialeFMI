#include <stdio.h>
#include <stdlib.h>
#include "text.in"

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<n;i++){
        for(int j=i+1;j<=n;j++){
            if(sumad(i)==j || sumad(j)==i){
                printf("(%d,%d)\n",i,j);
            }
        }
    }
    return 0;
}
