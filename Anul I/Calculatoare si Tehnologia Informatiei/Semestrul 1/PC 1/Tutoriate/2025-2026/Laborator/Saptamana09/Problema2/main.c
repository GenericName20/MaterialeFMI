#include <stdio.h>
#include <stdlib.h>

int **a,**b,c[100][100];
int n1,n2,m1,m2;

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");

    ///Citire a
    fscanf(fin,"%d %d",&n1,&m1);
    a = (int**) malloc(sizeof(int) * n1);
    for(int i=0;i<n1;i++){
        *(a+i) = (int*) malloc(sizeof(int) * (i+1));
        for(int j=0;j<i+1;j++){
            fscanf(fin,"%d",&a[i][j]);
        }
        for(int j=i+1;j<m1;j++){
            int x;
            fscanf(fin,"%d",&x);
        }
    }

    ///Citire b
    fscanf(fin,"%d %d",&n2,&m2);
    b = (int**) malloc(sizeof(int) * n2);
    for(int i=0;i<n2;i++){
        *(b+i) = (int*) malloc(sizeof(int) * (n2-i));
        for(int j=0;j<i;j++){
            int x;
            fscanf(fin,"%d ",&x);
        }
        for(int j=i;j<n2;j++){
            fscanf(fin,"%d",&b[i][j-i]);
            ///printf("%d ",b[i][j]);
        }
    }

    for(int i=0;i<n2;i++){
        for(int h=0;h<m2;h++){
            for(int j=0;j<m1;j++){
                int par1,par2;
                if(j>i || j>h){
                    par1=0;
                    par2=0;
                }
                else{
                    par1=a[i][j];
                    par2=b[j][h-j];
                }
                printf("%d %d\n",par1,par2);
                c[i][h]+=par1*par2;
            }
        }
    }

    ///Afisare a si b
    fprintf(fout,"Matricea A:\n");
    for(int i=0;i<n1;i++){
        for(int j=0;j<i+1;j++){
            fprintf(fout,"%d ",a[i][j]);
        }
        fprintf(fout,"\n");
    }
    fprintf(fout,"Matricea B:\n");
    for(int i=0;i<n2;i++){
        for(int j=0;j<n2-i;j++){
            fprintf(fout,"%d ",b[i][j]);
        }
        fprintf(fout,"\n");
    }
    fprintf(fout,"Matricea A*B:\n");
    for(int i=0;i<n1;i++){
        for(int j=0;j<m2;j++){
            fprintf(fout,"%d ",c[i][j]);
        }
        fprintf(fout,"\n");
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
