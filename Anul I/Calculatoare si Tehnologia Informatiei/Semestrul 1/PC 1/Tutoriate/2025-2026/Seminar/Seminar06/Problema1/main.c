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
    int v[n];
    for(int i=0;i<n;i++){
        fscanf(fin,"%d",&v[i]);
    }
    ///SORTARE CRESCATOR
    qsort(v, n, sizeof(int), cresc);
    for(int i=0;i<n;i++){
        fprintf(fout,"%d ",v[i]);
    }
    fprintf(fout,"\n");
    ///SORTARE DESCRESCATOR
    qsort(v, n, sizeof(int), descresc);
    for(int i=0;i<n;i++){
        fprintf(fout,"%d ",v[i]);
    }
    fprintf(fout,"\n");
    return 0;
}
