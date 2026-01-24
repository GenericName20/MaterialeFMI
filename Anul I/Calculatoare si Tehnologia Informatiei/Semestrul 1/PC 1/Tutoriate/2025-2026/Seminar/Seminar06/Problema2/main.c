#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cresc(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}
int descresc(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int main()
{
    ///CITIRE
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    int n;
    fscanf(fin,"%d",&n);
    int hf;
    if(n%2==0)hf=n/2;
    else hf=n/2+1;
    int v[hf],a[hf];
    for(int i=0;i<hf;i++){
        fscanf(fin,"%d",&v[i]);
    }
    for(int i=hf;i<n;i++){
        fscanf(fin,"%d",&a[i-hf]);
    }
    ///SORTARE CRESCATOR
    qsort(v, hf, sizeof(int), cresc);
    ///SORTARE DESCRESCATOR
    qsort(a, n-hf+1, sizeof(int), descresc);
    for(int i=0;i<hf;i++){
        fprintf(fout,"%d ",v[i]);
    }
    for(int i=hf;i<n;i++){
        fprintf(fout,"%d ",a[i-hf]);
    }
    return 0;
}
