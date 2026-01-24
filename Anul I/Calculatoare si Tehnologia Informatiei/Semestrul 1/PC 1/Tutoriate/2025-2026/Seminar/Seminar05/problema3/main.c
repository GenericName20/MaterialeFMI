#include <stdio.h>
#include <stdlib.h>

int n,m;
int a[100][100];

void swap(int *a,int *b){
    int aux=*a;
    *a=*b;
    *b=aux;
}

void func(int nrl,int nrc,int i,int j){
    for(int h=0;h<m;h++){
        swap(&*(*(a+i)+h),&*(*(a+j)+h));
    }
}

int main()
{
    FILE *fin = fopen("text.in","r");
    FILE *fout = fopen("text.out","w");
    fscanf(fin,"%d %d",&n,&m);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            fscanf(fin,"%d",&a[i][j]);
        }
    }

    func(n,m,0,2);

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            fprintf(fout,"%d ",a[i][j]);
        }
        fprintf(fout,"\n");
    }
    return 0;
}
