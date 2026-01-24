#include <stdio.h>
#include <stdlib.h>

int n;
int **a;

int compare1(const void* a, const void* b) {
   return (*(int*)a - *(int*)b);
}

int compareRows(const void *p1, const void *p2) {
    int index1 = ((int **)p1 - a);
    int index2 = ((int **)p2 - a);
    return a[0][index1] - a[0][index2];
}

void swap(int **row1, int **row2, int *size1, int *size2) {
    int *tempRow = *row1;
    *row1 = *row2;
    *row2 = tempRow;
    int tempSize = *size1;
    *size1 = *size2;
    *size2 = tempSize;
}

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout= fopen("text.out","w");
    fscanf(fin,"%d",&n);
    int pozs=1;
    a=(int**) malloc((n+1)*sizeof(int));
    a[0] = (int*) malloc((n+1)*sizeof(int));
    for(int i=1;i<=n;i++){
        int m;
        fscanf(fin,"%d",&m);
        a[0][pozs]=m;
        pozs++;
        *(a+i)=(int*) malloc( m* sizeof(int));
        for(int j=0;j<m;j++){
            fscanf(fin,"%d ",&a[i][j]);
        }
    }
    for (int i = 1; i <= n - 1; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (a[0][i] > a[0][j]) {
                swap(&a[i], &a[j], &a[0][i], &a[0][j]);
            }
        }
    }
    for(int i=1;i<=n;i++){
        int maxim=a[0][i];
        qsort(*(a+i), maxim, sizeof(int), compare1);

        for(int j=0;j<maxim;j++) fprintf(fout,"%d ",*(a[i]+j));
        fprintf(fout,"\n");
    }
    free(a);
    return 0;
}
