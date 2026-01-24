#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    return strcmp((const char*)a, (const char*)b);
}
int main()
{
    ///CITIRE
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    int n;
    fscanf(fin,"%d",&n);
    char a[n][100];
    for(int i=0;i<n;i++){
        fscanf(fin,"%s",a[i]);
    }
    qsort(a, n, sizeof(a[0]), cmp);
    for(int i=0;i<n;i++){
        fprintf(fout,"%s\n",a[i]);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
