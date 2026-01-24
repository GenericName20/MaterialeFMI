#include <stdio.h>
#include <stdlib.h>

void citafis(FILE *file)
{
    int n, **v;
    fscanf(file, "%d", &n);
    v = (int **)malloc(n * sizeof(int*));
    for(int i = 0; i < n; i++)
    {
        v[i] = malloc((i+1) * sizeof(int));
        for( int j = 0; j <= i; j++)
        {
            fscanf(file, "%d", &v[i][j]);
        }
    }
    for(int i = 0; i < n; i++)
    {
        for( int j = 0 ; j <= i; j++)
        {
            printf("%d ", v[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int **p, n;
    FILE *file = fopen("mat.txt", "r");
    //citafis(file);
    FILE *file1 = fopen("mat1.txt", "r");
    fscanf(file1, "%d", &n);
    p = (int **)malloc(n * sizeof(int *));
    for(int i = 0; i < n; i++)
    {
        p[i]=malloc((n-i) * sizeof(int));
        for(int j = 0; j < n-i; j++)
        {
            fscanf(file1, "%d", &p[i][j]);
        }
    }
    for(int i = 0; i < n; i++)
    {
        for( int j = 0 ; j < n-i; j++)
        {
            printf("%d ", p[i][j]);
        }
        printf("\n");
    }
    return 0;
}

