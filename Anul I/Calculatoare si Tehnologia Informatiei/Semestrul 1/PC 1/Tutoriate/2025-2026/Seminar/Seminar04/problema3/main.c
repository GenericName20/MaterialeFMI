#include <stdio.h>
#include <stdlib.h>

void cifre(int x,int *cmin,int* cmax){
    *cmin=9,*cmax=0;
    int ult;
    while(x){
        ult = x%10;
        if(ult>*cmax){
            *cmax=ult;
        }
        if(ult>*cmax){
            *cmax=ult;
        }
        x=x/10;
    }
}

void Comparare(int comp,int v[],int n){
    int cmin,cmax;
    for(int i=1;i<=n;i++){
        Cifre(v[i],&cmin,&cmax);
        if(v[i]<=comp && cmin==cmax){
            printf("%d ",v[i]);
        }
    }
}

int main()
{
    int n,comp,v[100];
    scanf("%d %d", &n,&comp);
    for(int i=1;i<=n;i++){
        scanf("%d",&v[i]);
    }
    Comparare(comp,v,n);
    return 0;
}
