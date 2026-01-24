#include <stdio.h>
#include <stdlib.h>

int cau(int v[],int poz,int n){
    for(int i=1;i<=n;i++){
        if(v[i]==poz)
            return i;
    }
    return -1;
}

int cautare(int v[],int poz,int *scomp,int n){
    return (*comp)(v,poz,n);
}

int v[1005];

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    int n;
    fscanf(fin,"%d",&n);
    for(int i=1;i<=n;i++){
        fscanf(fin,"&d",&v[i]);
    }
    int poz=0;
    fscanf(fin,"%d",poz);

    void (*comp)(int) = &cau;
    fprintf(fout,"%d",cautare(v,poz,&comp,n));
    return 0;
}
