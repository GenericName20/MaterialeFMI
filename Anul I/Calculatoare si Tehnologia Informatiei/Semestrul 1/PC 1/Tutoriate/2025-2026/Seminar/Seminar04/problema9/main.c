#include <stdio.h>
int n,a[10][10];
void matrice(int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(i>j) a[i][j]=i-j;
            else a[i][j]=j-i;
        }
    }
}
void afisare()
{
    int i,j;
    FILE *f;
    f=fopen("matrice.txt","w");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++) fprintf(f,"%d ",a[i][j]);
        fprintf(f,"\n");
    }
    fclose(f);
}
void interschimbare(int x,int y)
{
    int i,aux;
    for(i=0;i<n;i++)
    {
        aux=a[x][i];
        a[x][i]=a[y][i];
        a[y][i]=aux;
    }
}
int main()
{
    int x,y,i,j;
    scanf("%d",&n);
    matrice(n);
    afisare();
    scanf("%d %d",&x,&y);
    interschimbare(x,y);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++) printf("%d ",a[i][j]);
        printf("\n");
    }
    return 0;
}
