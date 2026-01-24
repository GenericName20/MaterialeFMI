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
    int n,reza=0;
    fscanf(fin,"%d",&n);
    char a[n][1005];
    for(int i=0;i<n;i++){
        fscanf(fin,"%s",a[i]);
        for(int j=0;j<=strlen(a[i]);j++){
            if(isalnum(a[i][j])){
                reza++;
                printf("%c",a[i][j]);
            }
        }
    }
    ///qsort(a, n, sizeof(a[0]), cmp);

    ///A
    fprintf(fout,"%d\n",reza);
    ///B
    for(int i=0;i<strlen(a[2]);i++){
        if(a[2][i]=='a' || a[2][i]=='e' || a[2][i]=='i' || a[2][i]=='o' || a[2][i]=='u'){
            for(int j=strlen(a[2])+1;j>i;j--){
                a[2][j]=a[2][j-1];
            }
            i++;
        }
    }
    for(int i=0;i<n;i++){
        fprintf(fout,"%s\n",a[i]);
    }
    ///C
    fprintf(fout,"\n%s",a[0]);
    fclose(fin);
    fclose(fout);
    return 0;
}
