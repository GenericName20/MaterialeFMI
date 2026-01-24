#include <stdio.h>

int maxvector(int n,int v[],int max,int i){
    //printf("%d %d\n",i,max);
    if(i==n){
        return max;
    }
    if(v[i]>max){
        max=v[i];
    }
    return maxvector(n,v,max,i+1);
}

int v[105];

int main() {
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        int cifra;
        scanf("%d",&v[i]);
    }
    printf("%d",maxvector(n,v, -1,0));
    return 0;
}