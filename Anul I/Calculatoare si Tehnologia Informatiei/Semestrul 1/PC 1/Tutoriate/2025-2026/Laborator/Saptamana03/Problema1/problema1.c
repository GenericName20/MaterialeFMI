#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE* fin=fopen("file.in","r");
    int n,m;
    int v[4005];
    fscanf(fin,"%d%d",&n,&m);
    for(int i=0;i<n;i++){
        int x;
        fscanf(fin,"%d",&x);
        if(x<0)
            v[x*2]=1;
        else
            v[x]=1;
    }
    for(int i=0;i<m;i++){
        int x;
        fscanf(fin,"%d",&x);
        if(x<0){
            if(v[x*2]==1)
                v[x*2]=2;
        }
        else{
            if(v[x]==1)
                v[x]=2;
        }
    }
    int rez=0;
    for(int i=0;i<m+n;i++){
        if(v[i]==2){
            rez++;
        }
    }
    printf("%d",rez);
    return 0;
}
