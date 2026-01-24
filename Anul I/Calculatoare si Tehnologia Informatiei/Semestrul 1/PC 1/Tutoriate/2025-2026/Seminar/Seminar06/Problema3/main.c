#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *a, const void *b) {
    return (*(char*)a - *(char*)b);
}

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");
    char v[1024];
    fscanf(fin,"%s",v);
    qsort(v, strlen(v), sizeof(char), comp);
    fprintf(fout,"%s",v);
    return 0;
}
