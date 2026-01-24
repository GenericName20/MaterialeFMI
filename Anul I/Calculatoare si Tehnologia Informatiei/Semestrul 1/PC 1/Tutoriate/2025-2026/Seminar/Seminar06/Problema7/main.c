#include<stdlib.h>
#include<stdio.h>
#include<string.h>

char *citire()
{
    char *aux=NULL, *p=NULL;
    size_t size=0, i=0;
    int c;
    c=EOF;
    while(c)
    {
        c=getc(stdin);
        if(c==EOF || c=='\n')
        {
            c=0;
        }
        if(size<=i)
        {
            size++;
            aux=(char*)realloc(p, size * sizeof(char));
            if(!aux)
            {
                free(p);
                p=NULL;
                break;
            }
            p=aux;
        }
        p[i++]=c;
    }
    return p;
}

char* concat(int n, char *a[])
{
    char *b;
    b=(char*)malloc(sizeof(char));
    size_t size=0;
    for(int i=0; i<n; i++)
    {
        b=(char*)realloc(b, size+strlen(a[i])*sizeof(char));
        size+=strlen(a[i])*sizeof(char);
        strcat(b, a[i]);
    }
    return b;
}

int main()
{
    char *b;
    int n;
    scanf("%d", &n);
    char **a = (char**)malloc(n * sizeof(char*));
    getc(stdin);
    for(int i=0; i<n; i++)
    {
        a[i]=citire();
    }
    b=concat(n, a);
    printf("%s", b);
    free(a);
    free(b);
    return 0;
}
